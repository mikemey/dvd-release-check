prefix = "https://api.themoviedb.org/3/discover/movie"
api = "?api_key={API_KEY}"

query_template = "&language=en" \
                 "&release_date.gte={LOWER_DATE}&release_date.lte={UPPER_DATE}" \
                 "&primary_release_date.gte={LOWER_DATE}&primary_release_date.lte={UPPER_DATE}"

test_query = query_template \
    .replace("{LOWER_DATE}", "2015-08-09") \
    .replace("{UPPER_DATE}", "2015-08-16")

sort = "&sort_by=popularity.desc"

testSearchUrl = prefix + api + test_query + sort
searchUrl = prefix + api + query_template + sort

urls = {
    'fight_club': "https://api.themoviedb.org/3/movie/550?api_key={API_KEY}",
    'api_key_error': "https://api.themoviedb.org/3/movie/550?api_key={API_KEY}k",
    'test_search_releases': testSearchUrl,
    'search_releases': searchUrl
}
