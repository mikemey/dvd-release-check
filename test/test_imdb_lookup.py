from imdb_lookup import ImdbLookup
from logTestCase import LogTestCase


class TestImdbRatings(LogTestCase):
    def test_imdb_rating(self):
        expected_rating = 9.2
        expected_genres = ['Crime', 'Drama']
        actual = ImdbLookup().find_movie_data("The Godfather")

        self.quickEquals(actual.rating, expected_rating)
        self.quickEquals(actual.genres, expected_genres)

    def test_no_imdb_rating(self):
        expected = None
        actual = ImdbLookup().find_movie_data("Farhope Tower")

        self.quickEquals(actual.rating, expected)
