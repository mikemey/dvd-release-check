import datetime
import json
import os

import requests

from mlc_commons import logger
from mlc_model import MovieItem

api_key = os.environ['DRC_MOVIEDB_API_KEY']


def convert_movies(results):
    movies = []
    for result in results:
        if "en" != result['original_language']:
            continue

        title = result['original_title']
        pop = result['popularity'] if "popularity" in result else 0.0
        movies.append(MovieItem(title, pop))

    return movies


def fill_dates(url_template, end_date):
    week = datetime.timedelta(days=7)
    lower_date = end_date - week

    return url_template \
        .replace("{LOWER_DATE}", lower_date.strftime("%Y-%m-%d")) \
        .replace("{UPPER_DATE}", end_date.strftime("%Y-%m-%d"))


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

        return convert_movies(loaded['data']['results'])
