import os

from mlc_model import MovieReleaseMail

base_path = os.path.dirname(__file__) + "/"


class MailGen:
    def __init__(self):
        self.email_template = self.load_email_template()
        self.row_template = """\n        <tr> <td class="rating">{}</td> <td>{}</td> <td class="pop">{}</td> </tr>"""

    def create_email(self, movies):
        titles = ""
        for movie in movies:
            popularity = round(movie.pop, 1)
            rating = movie.rating or "n/a"
            titles += self.row_template.format(rating, movie.title, popularity)

        email_body = self.email_template % titles
        return MovieReleaseMail(email_body)

    @staticmethod
    def load_email_template():
        return open(base_path + "resources/mlc_mail_template.html") \
            .read() \
            .replace("%", "%%") \
            .replace("{titles}", "%s")
