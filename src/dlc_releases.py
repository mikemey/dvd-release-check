import datetime
import json
import os

import requests

from dlc_commons import logger
from dlc_model import MovieItem

api_key = os.environ['DRC_TIMES_API_KEY']


def convert_movies(results):
    movies = []
    for result in results:
        title = result['display_title']
        pop = result['popularity'] if "popularity" in result else None
        movies.append(MovieItem(title, pop))

    return movies


def fill_dates(url_template, end_date):
    week = datetime.timedelta(days=7)
    lower_date = end_date - week

    return url_template \
        .replace("{LOWER_DATE}", lower_date.strftime("%Y-%m-%d")) \
        .replace("{UPPER_DATE}", end_date.strftime("%Y-%m-%d"))


class DvdReleases:
    def __init__(self, url):
        self.url = url

    def load(self):
        logger.info("loading data...")

        today = datetime.datetime.today()
        search_url = fill_dates(self.real_url(), today)
        resp = requests.get(search_url)

        if resp.status_code != 200:
            message = "Response was: %s %s" % (resp.status_code, resp.reason)
            logger.info("loading data failed: [%s]" % message)
            json_response = json.loads("""{ "error": "%s" }""" % message)
        else:
            json_response = json.loads(resp.content)
            logger.info("data loaded. results count: [%s]" % len(json_response['results']))

        return json_response

    def real_url(self):
        return self.url.replace("{API_KEY}", api_key)

    def last_weeks_releases(self):
        loaded = self.load()
        if "error" in loaded:
            return loaded

        return convert_movies(loaded['results'])
