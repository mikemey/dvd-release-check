import logging
import os
import sys

# the movie db parameters:
# ---------------------------------


class MovieDB:

    def __init__(self):
        pass

        self.prefix = "https://api.themoviedb.org/3/discover/movie"
        self.api = "?api_key={API_KEY}"

        self.query_template = "&language=en" \
                              "&release_date.gte={LOWER_DATE}&release_date.lte={UPPER_DATE}" \
                              "&primary_release_date.gte={LOWER_DATE}&primary_release_date.lte={UPPER_DATE}"

        self.test_query = self.query_template \
            .replace("{LOWER_DATE}", "2013-08-09") \
            .replace("{UPPER_DATE}", "2013-08-16")

        self.sort = "&sort_by=popularity.desc"

        self.testSearchUrl = self.prefix + self.api + self.test_query + self.sort
        self.searchUrl = self.prefix + self.api + self.query_template + self.sort


movie_db = MovieDB()
urls = {
    'fight_club': "https://api.themoviedb.org/3/movie/550?api_key={API_KEY}",
    'api_key_error': "https://api.themoviedb.org/3/movie/550?api_key={API_KEY}k",
    'test_search_releases': movie_db.testSearchUrl,
    'search_releases': movie_db.searchUrl
}

# IMDB settings:
# ---------------------------------


class Imdb:
    api_key = os.environ['DRC_MOVIEDB_API_KEY']

    def __init__(self):
        pass

# logging settings:
# ---------------------------------
logging.addLevelName(logging.WARNING, "WARN")
root = logging.getLogger()
root.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)5s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

logger = logging.getLogger("dlc")

logging.getLogger("requests").setLevel(logging.WARN)
