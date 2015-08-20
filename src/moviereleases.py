import datetime
import json
import logging

import requests

apikey = "c1b8c43af9af6b592db8570437bf2e70"

logger = logging.getLogger("dlc")


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

        return_val += """ { "title": "%s", "rating": %s }""" % \
                      (title, pop)
    return_val += " ] }"
    return return_val


def fill_dates(url_template, end_date):
    week = datetime.timedelta(days=7)
    lower_date = end_date - week

    return url_template \
        .replace("{LOWER_DATE}", lower_date.strftime("%Y-%m-%d")) \
        .replace("{UPPER_DATE}", end_date.strftime("%Y-%m-%d"))


def create_email(data):
    email_body = """<html>\n""" \
                 """<body>\n""" \
                 """<div style="font-family: 'Arial';">\n""" \
                 """<h3>New movie releases:</h3>\n""" \
                 """<table style="width: 100%; max-width: 400px">"""

    for doc in data['docs']:
        rating = round(doc['rating'], 1)
        email_body += """\n<tr> <td>{}</td> <td align="right">{}</td> </tr>""".format(doc['title'], rating)

    email_body += """\n</table>\n""" \
                  """<h4>Your Movie release check!</h4></div>\n""" \
                  """</body>\n""" \
                  """</html>\n"""

    return MovieReleaseMail(email_body)


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
        return self.url.replace("{API_KEY}", apikey)

    def last_weeks_releases(self):
        loaded = self.load()
        if "error" in loaded:
            return loaded

        json_str = json_titles(loaded['data']['results'])
        return json.loads(json_str)
