import datetime
import json
from unittest import TestCase

from moviereleases import MovieReleases, json_titles, fill_dates, create_email
from mlc_commons import urls


class TestDvdRelease(TestCase):
    def setUp(self):
        test_class = self.__class__.__name__
        test_method = self._testMethodName

        print """--------------\nTest run: [%s - %s]""" % (test_class, test_method)

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

        result_count = actual['docs'].__len__()

        print "Result count: " + repr(result_count)
        self.assertGreater(result_count, 0,
                           "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (result_count, 0))

    def test_json_titles(self):
        test_input = """[
                { "original_title": "t1", "original_language": "en", "popularity": 3.3 }
                , { "original_title": "t2", "original_language": "some_other" }
                , { "original_title": "t3", "original_language": "en" }
                ]"""

        actual_titles = json_titles(json.loads(test_input))
        expected_json = """{ "docs": [ { "title": "t1", "rating": 3.3 }, { "title": "t3", "rating":  } ] }"""
        self.assertEquals(actual_titles, expected_json,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (json_titles, expected_json))

    def test_create_email(self):
        releases = MovieReleases(urls['test_search_releases'])
        data = releases.last_weeks_releases()

        email = create_email(data)

        expected_subject = "Movie releases"
        self.assertEquals(email.subject, expected_subject,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (email.subject, expected_subject))
        self.assertTrue(email.content.__len__() > 0, "Content not set!")

    def test_create_popularity(self):
        test_input = """{ "docs": [
                { "title": "t1", "rating": 12.344 }
                , { "title": "t2", "rating": 9.39 }
                , { "title": "t3", "rating": 0.555 }
                ] }"""

        email = create_email(json.loads(test_input.capitalize()))

        import difflib

        expected = test_email_content.splitlines(True)
        actual = email.content.splitlines(True)

        diff = difflib.unified_diff(expected, actual)
        diff_msg = ''.join(diff)

        self.assertTrue(diff_msg.__len__() == 0, "Content differs: \n%s" % diff_msg)


test_email_content = open("resources/test_mail_content.html").read()
