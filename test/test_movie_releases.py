import datetime
import json

from logTestCase import LogTestCase
from movie_releases import MovieReleases, convert_movies, fill_dates, MovieItem
from mlc_commons import urls


class TestDvdRelease(LogTestCase):
    def callLoad(self, url):
        return MovieReleases(url).load()

    def test_connection_load_movie(self):
        expected = "Fight Club"
        actual = self.callLoad(urls['fight_club'])
        title = actual['data']['original_title']

        self.assertEquals(title, expected,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (title, expected))

    def test_invalid_api_key(self):
        expected_message = "Invalid API key: You must be granted a valid key."
        actual = self.callLoad(urls['api_key_error'])

        self.assertEquals(actual["error"], expected_message,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (actual, expected_message))

    def test_load_week(self):
        expected_count = 192
        actual = self.callLoad(urls['test_search_releases'])

        result_count = actual['data']['total_results']

        self.assertEquals(result_count, expected_count,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (result_count, expected_count))

    def test_fill_dates(self):
        url_template = "http://bla.bla?lower={LOWER_DATE}&upper={UPPER_DATE}"
        end_date = datetime.date(2015, 04, 02)
        fill_dates_result = fill_dates(url_template, end_date)

        expected_url = "http://bla.bla?lower=2015-03-26&upper=2015-04-02"

        self.assertEquals(fill_dates_result, expected_url,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (fill_dates_result, expected_url))

    def test_load_current_week(self):
        actual = MovieReleases(urls['search_releases']).last_weeks_releases()

        result_count = len(actual)

        print "Result count: " + repr(result_count)
        self.assertGreater(result_count, 0,
                           "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (result_count, 0))

    def test_convert_movies(self):
        test_input = """[
                { "original_title": "t1", "original_language": "en", "popularity": 3.3 }
                , { "original_title": "t2", "original_language": "some_other" }
                , { "original_title": "t3", "original_language": "en" }
                ]"""

        actual_movies = convert_movies(json.loads(test_input))
        expected_movies = [
            MovieItem("t1", 3.3),
            MovieItem("t3", 0.0)
        ]

        self.assertEqual(len(actual_movies), len(expected_movies))
        self.assert_movie(0, actual_movies, expected_movies)
        self.assert_movie(1, actual_movies, expected_movies)

    def assert_movie(self, index, actual, expected):
        self.assertEquals(actual[index].title, expected[index].title,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (actual[index].title, expected[index].title))
        self.assertEquals(actual[index].pop, expected[index].pop,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (actual[index].pop, expected[index].pop))
