import imdb


class ImdbLookup:
    def __init__(self):
        self.imdb = imdb.IMDb('http')
        pass

    def find_rating(self, movie_title):
        movie_info = self.imdb.search_movie(movie_title, 1)[0]
        movie = self.imdb.get_movie(movie_info.movieID)
        return movie.get("rating", None)
