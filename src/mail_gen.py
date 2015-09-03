import os

from drc_model import MovieReleaseMail

base_path = os.path.dirname(__file__) + "/"


def load_email_template():
    return open(base_path + "resources/drc_mail_template.html") \
        .read() \
        .replace("%", "%%") \
        .replace("{titles}", "%s")


def get_or_else(movie, key, default, function_or_none=None):
    attr = getattr(movie, key, None)
    if attr:
        if function_or_none:
            return function_or_none(attr)
        return attr
    return default


class MailGen:
    def __init__(self):
        self.email_template = load_email_template()
        self.row_template = """\n<tr> <td class="rating">{}</td> <td>{}</td> <td class="genres">{}</td> </tr>"""

    def create_email(self, movies):
        titles = ""
        for movie in movies:
            rating = get_or_else(movie, "rating", "n/a")
            genres = get_or_else(movie, "genres", "", lambda x: " ".join(x))
            titles += self.row_template.format(rating, movie.title, genres)

        email_body = self.email_template % titles
        return MovieReleaseMail(email_body)
