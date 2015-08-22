import datetime
import json
import os

import requests

from mlc_commons import base_path, logger

api_key = os.environ['DRC_MOVIEDB_API_KEY']


def json_titles(results):
    return_val = """{ "docs": ["""

    first = True
    for result in results:
        if "en" != result['original_language']:
            continue

        if not first:
            return_val += ","
        first = False

        title = result['original_title']
        pop = result['popularity'] if "popularity" in result else ""

        return_val += """ { "title": "%s", "rating": %s }""" % (title, pop)

    return_val += " ] }"
    return return_val


def fill_dates(url_template, end_date):
    week = datetime.timedelta(days=7)
    lower_date = end_date - week

    return url_template \
        .replace("{LOWER_DATE}", lower_date.strftime("%Y-%m-%d")) \
        .replace("{UPPER_DATE}", end_date.strftime("%Y-%m-%d"))


def create_email(data):
    row_template = """\n        <tr> <td class="count">{}</td> <td>{}</td> <td class="rate">{}</td> </tr>"""

    titles = ""
    for idx, doc in enumerate(data['docs']):
        rating = round(doc['rating'], 1)
        titles += row_template.format(idx + 1, doc['title'], rating)

    email_body = email_template() % titles
    return MovieReleaseMail(email_body)


def email_template():
    return open(base_path + "resources/mlc_mail_template.html") \
        .read() \
        .replace("%", "%%") \
        .replace("{titles}", "%s")


class MovieReleaseMail:
    def __init__(self, email_content):
        self.subject = "Movie releases"
        self.content = email_content


class MovieReleases:
    def __init__(self, url):
        self.url = url

    def load(self):
        logger.info("loading data...")

        today = datetime.datetime.today()
        search_url = fill_dates(self.real_url(), today)
        resp = requests.get(search_url)

        if resp.status_code != 200:
            json_body = resp.json()
            message = json_body['status_message']
            logger.info("loading data failed: [%s]" % message)
            data_json = """{ "error": "%s" }""" % message
        else:
            logger.info("data loaded.")
            data_json = """{ "data": %s }""" % resp.content

        return json.loads(data_json)

    def real_url(self):
        return self.url.replace("{API_KEY}", api_key)

    def last_weeks_releases(self):
        loaded = self.load()
        if "error" in loaded:
            return loaded

        json_str = json_titles(loaded['data']['results'])
        return json.loads(json_str)
