from imdb_lookup import ImdbLookup
from imdb_ratings import ImdbRatings
from logTestCase import LogTestCase
from dlc_model import MovieItem

test_movie1 = MovieItem('movie1', 6.6, 4.2)
test_movie2 = MovieItem('movie2', 8.88, 5.5)
test_movie3 = MovieItem('movie3', None, None)
test_movie4 = MovieItem('movie4', 5.88, 6.5)


class TestImdbRatings(LogTestCase):
    def test_ratings_added(self):
        ratings = ImdbRatings(LookupImdbMock())

        data = self.create_movie_data()

        enhanced_data = ratings.enhance_data(data)

        self.assert_movie_equals(enhanced_data[0], test_movie4)
        self.assert_movie_equals(enhanced_data[1], test_movie2)
        self.assert_movie_equals(enhanced_data[2], test_movie1)
        self.assert_movie_equals(enhanced_data[3], test_movie3)

    def create_movie_data(self):
        return [test_movie1, test_movie2, test_movie3, test_movie4]

    def assert_movie_equals(self, data, expected):
        self.assert_data_equals(data.title, expected.title)
        self.assert_data_equals(data.pop, expected.pop)
        self.assert_data_equals(data.rating, expected.rating)

    def assert_data_equals(self, actual, expected):
        self.quickEquals(actual, expected)


class LookupImdbMock(ImdbLookup):
    title_movie_map = {
        test_movie1.title: test_movie1,
        test_movie2.title: test_movie2,
        test_movie3.title: test_movie3,
        test_movie4.title: test_movie4
    }

    def find_rating(self, movie_title):
        return self.title_movie_map[movie_title].rating
