class MovieItem:
    def __init__(self, title, pop, rating=None):
        self.title = title
        self.rating = rating
        self.pop = pop


class MovieReleaseMail:
    def __init__(self, email_content, subject="Movie releases"):
        self.subject = subject
        self.content = email_content
