import imdb

from drc_model import MovieData


class ImdbLookup:
    def __init__(self):
        self.imdb = imdb.IMDb('http')
        pass

    def find_movie_data(self, movie_title):
        movie_info = self.imdb.search_movie(movie_title, 1)[0]
        movie = self.imdb.get_movie(movie_info.movieID)
        return MovieData(movie.get("rating", None),
                         movie.get("genres", None))
