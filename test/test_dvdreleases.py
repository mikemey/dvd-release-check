import datetime
from unittest import TestCase

from dvdrelease import DvdRelease
from tmdburl import urls


class TestDvdRelease(TestCase):
    def setUp(self):
        test_class = self.__class__.__name__
        test_method = self._testMethodName

        print """--------------\nTest run: [%s - %s]""" % (test_class, test_method)

    def callLoad(self, url):
        return DvdRelease(url).load()

    def test_connection_load_movie(self):
        expected = "Fight Club"
        actual = self.callLoad(urls['fight_club'])
        title = actual['data']['original_title']

        self.assertEquals(title, expected,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (title, expected))

    def test_invalid_api_key(self):
        expected = "{ 'error': 'Invalid API key: You must be granted a valid key.'}"
        actual = self.callLoad(urls['api_key_error'])

        self.assertEquals(actual, expected,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (actual, expected))

    def test_load_week(self):
        expected_count = 91
        actual = self.callLoad(urls['test_search_releases'])

        result_count = actual['data']['total_results']

        self.assertEquals(result_count, expected_count,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (result_count, expected_count))

    def test_fill_dates(self):
        url_template = "http://blabla?lower={LOWER_DATE}&upper={UPPER_DATE}"
        end_date = datetime.date(2015, 04, 02)
        fill_dates_result = DvdRelease(url_template).fillDates(url_template, end_date)

        expected_url = "http://blabla?lower=2015-03-26&upper=2015-04-02"

        self.assertEquals(fill_dates_result, expected_url,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (fill_dates_result, expected_url))

    def test_load_current_week(self):
        actual = DvdRelease(urls['search_releases']).lastWeeksReleases()

        result_count = actual['docs'].__len__()

        print "Result count: " + repr(result_count)
        self.assertGreater(result_count, 0,
                           "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (result_count, 0))

    def test_create_email(self):
        pass
