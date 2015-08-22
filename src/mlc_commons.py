import logging
import os

prefix = "https://api.themoviedb.org/3/discover/movie"
api = "?api_key={API_KEY}"

query_template = "&language=en" \
                 "&release_date.gte={LOWER_DATE}&release_date.lte={UPPER_DATE}" \
                 "&primary_release_date.gte={LOWER_DATE}&primary_release_date.lte={UPPER_DATE}"

test_query = query_template \
    .replace("{LOWER_DATE}", "2013-08-09") \
    .replace("{UPPER_DATE}", "2013-08-16")

sort = "&sort_by=popularity.desc"

testSearchUrl = prefix + api + test_query + sort
searchUrl = prefix + api + query_template + sort

urls = {
    'fight_club': "https://api.themoviedb.org/3/movie/550?api_key={API_KEY}",
    'api_key_error': "https://api.themoviedb.org/3/movie/550?api_key={API_KEY}k",
    'test_search_releases': testSearchUrl,
    'search_releases': searchUrl
}

base_path = os.path.dirname(__file__) + "/"

logging.addLevelName(logging.WARNING, "WARN")
logging.basicConfig(format='%(asctime)s %(levelname)5s - %(message)s')
logging.getLogger("dlc").setLevel(logging.INFO)

logger = logging.getLogger("dlc")
