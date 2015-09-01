from imdb_lookup import ImdbLookup
from logTestCase import LogTestCase


class TestImdbRatings(LogTestCase):
    def test_imdb_rating(self):
        expected = 9.2
        actual = ImdbLookup().find_rating("The Godfather")

        self.quickEquals(actual, expected)

    def test_no_imdb_rating(self):
        expected = None
        actual = ImdbLookup().find_rating("Farhope Tower")

        self.quickEquals(actual, expected)
