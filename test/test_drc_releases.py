import datetime
import json

from logTestCase import LogTestCase
from drc_model import MovieItem
from drc_releases import DvdReleases, convert_movies, fill_dates
from drc_commons import urls


class TestMovieReleases(LogTestCase):
    def callLoad(self, url):
        return DvdReleases(url).load()

    def test_connection_load_movie(self):
        expected_title = "Fight Club"
        expected_release = "2003-10-14"
        actual = self.callLoad(urls['fight_club'])

        result_count = len(actual['results'])

        self.quickEquals(result_count, 9)

        actual_title = actual['results'][3]['display_title']
        actual_dvd_release = actual['results'][3]['dvd_release_date']

        self.quickEquals(actual_title, expected_title)
        self.quickEquals(actual_dvd_release, expected_release)

    def test_invalid_api_key(self):
        expected_message = "Response was: 403 Forbidden"
        actual = self.callLoad(urls['api_key_error'])

        self.quickEquals(actual["error"], expected_message)

    def test_load_week(self):
        expected_count = 8
        actual = self.callLoad(urls['test_search_releases'])

        result_count = actual['num_results']

        self.assertGreater(result_count, expected_count)

    def test_fill_dates(self):
        url_template = "http://bla.bla?date={LOWER_DATE};{UPPER_DATE}"
        end_date = datetime.date(2015, 04, 02)
        fill_dates_result = fill_dates(url_template, end_date)

        expected_url = "http://bla.bla?date=2015-03-26;2015-04-02"
        self.quickEquals(fill_dates_result, expected_url)

    def test_load_current_week(self):
        actual = DvdReleases(urls['search_releases']).last_weeks_releases()
        self.quickEquals(len(actual), 20)

    def test_convert_movies(self):
        test_input = """[
                { "display_title": "t1", "original_language": "en", "popularity": 3.3 }
                , { "display_title": "t2" }
                , { "display_title": "t3", "original_language": "en" }
                ]"""

        actual_movies = convert_movies(json.loads(test_input))
        expected_movies = [
            MovieItem("t1", 3.3),
            MovieItem("t2", None),
            MovieItem("t3", None)
        ]
        self.assertEqual(len(actual_movies), len(expected_movies))
        for ix, expected_movie in enumerate(expected_movies):
            self.assert_movie(actual_movies[ix], expected_movies[ix])

    def assert_movie(self, actual, expected):
        self.quickEquals(actual.title, expected.title)
        self.quickEquals(actual.pop, expected.pop)
