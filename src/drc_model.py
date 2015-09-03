class MovieItem:
    def __init__(self, title, pop, movie_data=None):
        self.title = title
        self.pop = pop
        if movie_data:
            self.rating = movie_data.rating
            self.genres = movie_data.genres


class MovieData:
    def __init__(self, rating, genres):
        self.rating = rating
        self.genres = genres


class MovieReleaseMail:
    def __init__(self, email_content, subject="Movie releases"):
        self.subject = subject
        self.content = email_content
