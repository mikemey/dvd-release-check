from imdb_lookup import ImdbLookup
from logTestCase import LogTestCase


class TestImdbRatings(LogTestCase):
    def test_imdb_rating(self):
        expected = 9.2
        actual = ImdbLookup().find_rating("The Godfather")

        self.assertEqual(actual, expected, "\n\tactual  : [%s]\n\texpected: [%s]" % (actual, expected))

    def test_no_imdb_rating(self):
        expected = None
        actual = ImdbLookup().find_rating("Farhope Tower")

        self.assertEqual(actual, expected, "\n\tactual  : [%s]\n\texpected: [%s]" % (actual, expected))
