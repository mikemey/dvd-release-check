import sys
import math

progress_bar_length = 20
progress_char = "X"


def report(index, length):
    star_count = (index + 1.0) / length * progress_bar_length
    stars = ("{0}" * math.trunc(star_count)).format(progress_char)

    text = """Fetching imdb data: [{0:{1}s}]""".format(stars, progress_bar_length)
    print '\x1b[80D' + '\x1b[K' + text,
    sys.stdout.flush()


class ImdbRatings:
    def __init__(self, lookup):
        self.lookup = lookup

    def enhance_data(self, raw_movies):
        for ix, movie in enumerate(raw_movies):
            report(ix, len(raw_movies))

            movie_data = self.lookup.find_movie_data(movie.title)
            movie.rating = movie_data.rating
            movie.genres = movie_data.genres
        print
        return sorted(raw_movies, key=lambda m: m.rating, reverse=True)
