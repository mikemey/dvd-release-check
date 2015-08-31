import sys
import math

progress_bar_length = 20
progress_char = "X"


def report(index, length):
    star_count = (index + 1.0) / length * progress_bar_length
    stars = ("{0}" * math.trunc(star_count)).format(progress_char)

    text = """Fetching ratings: [{0:{1}s}]""".format(stars, progress_bar_length)
    print '\x1b[80D' + '\x1b[K' + text,
    sys.stdout.flush()


class ImdbRatings:
    def __init__(self, lookup):
        self.lookup = lookup

    def enhance_data(self, movie_data):
        for ix, movie in enumerate(movie_data):
            report(ix, len(movie_data))
            rating = self.lookup.find_rating(movie.title)
            movie.rating = rating

        return sorted(movie_data, key=lambda m: m.rating, reverse=True)
