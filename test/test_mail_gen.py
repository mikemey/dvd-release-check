import difflib

from logTestCase import LogTestCase
from mail_gen import MailGen
from mlc_model import MovieItem


class TestMailGen(LogTestCase):
    mail_gen = MailGen()

    def test_create_popularity(self):
        input_movies = [
            MovieItem("t1", 12.344),
            MovieItem("t2", 9.39),
            MovieItem("t3", 0.555)
        ]
        input_movies[0].rating = 4.4
        input_movies[1].rating = None
        input_movies[2].rating = 6.6

        email = self.mail_gen.create_email(input_movies)

        expected = test_email_content.splitlines(True)
        actual = email.content.splitlines(True)

        diff = difflib.unified_diff(expected, actual)
        diff_msg = ''.join(diff)

        self.assertTrue(diff_msg.__len__() == 0, "Content differs: \n%s" % diff_msg)


test_email_content = open("resources/test_mail_content.html").read()
