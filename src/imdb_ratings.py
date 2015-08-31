class ImdbRatings:
    def __init__(self, lookup):
        self.lookup = lookup

    def enhance_data(self, movie_data):
        for movie in movie_data:
            rating = self.lookup.find_rating(movie.title)
            movie.rating = rating

        return sorted(movie_data, key=lambda m: m.rating, reverse=True)
