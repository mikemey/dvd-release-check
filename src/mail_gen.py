from mlc_commons import base_path
from mlc_model import MovieReleaseMail


class MailGen:
    def __init__(self):
        self.email_template = self.load_email_template()
        self.row_template = """\n        <tr> <td class="rating">{}</td> <td>{}</td> <td class="pop">{}</td> </tr>"""
        pass

    def create_email(self, movies):
        titles = ""
        for movie in movies:
            popularity = round(movie.pop, 1)
            titles += self.row_template.format(movie.rating, movie.title, popularity)

        email_body = self.email_template % titles
        return MovieReleaseMail(email_body)

    @staticmethod
    def load_email_template():
        return open(base_path + "resources/mlc_mail_template.html") \
            .read() \
            .replace("%", "%%") \
            .replace("{titles}", "%s")
