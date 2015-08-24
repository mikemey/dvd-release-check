class MovieItem:
    def __init__(self, title, pop):
        self.title = title
        self.rating = 0.0
        self.pop = pop


class MovieReleaseMail:
    def __init__(self, email_content):
        self.subject = "Movie releases"
        self.content = email_content
