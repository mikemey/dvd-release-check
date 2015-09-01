import logging
import sys

# the movie db parameters:
# ---------------------------------


class MovieDB:
    def __init__(self):
        self.base_query = "http://api.nytimes.com/svc/movies/v2/reviews/search?api-key={API_KEY}&dvd=Y"

        self.query_template = "&publication-date={LOWER_DATE};{UPPER_DATE}"

        self.test_query = self.query_template \
            .replace("{LOWER_DATE}", "2015-02-09") \
            .replace("{UPPER_DATE}", "2015-03-16")

        self.sort = "&order=by-dvd-release-date"

        self.testSearchUrl = self.base_query + self.test_query + self.sort
        self.searchUrl = self.base_query + self.sort


movie_db = MovieDB()
urls = {
    'fight_club': movie_db.base_query + "&query=fight+AND+club&order=by-title&api-key={API_KEY}",
    'api_key_error': movie_db.base_query.replace("{API_KEY}", "a{API_KEY}b") + "&query=fight+AND+club",
    'test_search_releases': movie_db.testSearchUrl,
    'search_releases': movie_db.searchUrl
}

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
