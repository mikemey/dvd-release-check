import json

from imdb_lookup import ImdbLookup
from imdb_ratings import ImdbRatings
from logTestCase import LogTestCase


class TestMovie:
    def __init__(self, title, rating, pop):
        self.title = title
        self.rating = rating
        self.pop = pop


test_movie1 = TestMovie('movie1', 6.6, 2.2)
test_movie2 = TestMovie('movie2', 8.88, 5.55)


class TestImdbRatings(LogTestCase):
    def test_ratings_added(self):
        ratings = ImdbRatings(LookupImdbMock())

        data_str = """{"docs": [
            {"pop": %s,
             "title": "%s"
             },
            {"pop": %s,
             "title": "%s"
             }
        ]}""" % (test_movie1.pop, test_movie1.title, test_movie2.pop, test_movie2.title)

        data = json.loads(data_str)

        new_data = ratings.enhance_data(data)

        self.assert_movie_equals(new_data['docs'][0], test_movie2)
        self.assert_movie_equals(new_data['docs'][1], test_movie1)

    def assert_movie_equals(self, data, expected):
        self.assert_data_equals(data['title'], expected.title)
        self.assert_data_equals(data['pop'], expected.pop)
        self.assert_data_equals(data['rating'], expected.title)
        pass

    def assert_data_equals(self, actual, expected):
        self.assertEqual(actual, expected, "\n\tactual  : [%s]\n\texpected: [%s]" % (actual, expected))


class LookupImdbMock(ImdbLookup):
    title_movie_map = {
        test_movie1.title: test_movie1,
        test_movie2.title: test_movie2
    }

    def __init__(self):
        ImdbLookup.__init__(self)

    def find_rating(self, movie_title):
        return self.title_movie_map[movie_title].rating
