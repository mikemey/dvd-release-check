import os

from drc_model import MovieReleaseMail

base_path = os.path.dirname(__file__) + "/"


def load_email_template():
    return open(base_path + "resources/drc_mail_template.html") \
        .read() \
        .replace("%", "%%") \
        .replace("{titles}", "%s")


class MailGen:
    def __init__(self):
        self.email_template = load_email_template()
        self.row_template = """\n<tr> <td class="rating">{}</td> <td>{}</td> </tr>"""

    def create_email(self, movies):
        titles = ""
        for movie in movies:
            rating = movie.rating or "n/a"
            titles += self.row_template.format(rating, movie.title)

        email_body = self.email_template % titles
        return MovieReleaseMail(email_body)
