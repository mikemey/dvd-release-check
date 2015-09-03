from imdb_lookup import ImdbLookup
from imdb_ratings import ImdbRatings
from logTestCase import LogTestCase
from drc_model import MovieItem, MovieData

test_movie1 = MovieItem('movie1', 6.6, MovieData(4.2, []))
test_movie2 = MovieItem('movie2', 8.88, MovieData(5.5, ['Drama']))
test_movie3 = MovieItem('movie3', None, MovieData(None, ['Crime', 'Drama']))
test_movie4 = MovieItem('movie4', 5.88, MovieData(6.5, []))


class TestImdbRatings(LogTestCase):
    def test_ratings_added(self):
        ratings = ImdbRatings(LookupImdbMock())

        raw_movies = self.create_test_movies()

        enhanced_data = ratings.enhance_data(raw_movies)

        self.assert_movie_equals(enhanced_data[0], test_movie4)
        self.assert_movie_equals(enhanced_data[1], test_movie2)
        self.assert_movie_equals(enhanced_data[2], test_movie1)
        self.assert_movie_equals(enhanced_data[3], test_movie3)

    def create_test_movies(self):
        return [test_movie1, test_movie2, test_movie3, test_movie4]

    def assert_movie_equals(self, data, expected):
        self.assert_data_equals(data.title, expected.title)
        self.assert_data_equals(data.pop, expected.pop)
        self.assert_data_equals(data.rating, expected.rating)
        self.assert_data_equals(data.genres, expected.genres)

    def assert_data_equals(self, actual, expected):
        self.quickEquals(actual, expected)


class LookupImdbMock(ImdbLookup):
    title_movie_map = {
        test_movie1.title: test_movie1,
        test_movie2.title: test_movie2,
        test_movie3.title: test_movie3,
        test_movie4.title: test_movie4
    }

    def find_movie_data(self, movie_title):
        rating = self.title_movie_map[movie_title].rating
        genres = self.title_movie_map[movie_title].genres
        return MovieData(rating, genres)
