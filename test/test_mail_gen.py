import difflib

from logTestCase import LogTestCase
from mail_gen import MailGen
from movie_releases import MovieReleases, MovieItem
from mlc_commons import urls


class TestMailGen(LogTestCase):
    mail_gen = MailGen()

    def test_create_email(self):
        releases = MovieReleases(urls['test_search_releases'])
        data = releases.last_weeks_releases()

        email = self.mail_gen.create_email(data)

        expected_subject = "Movie releases"
        self.assertEquals(email.subject, expected_subject,
                          "Error:\n\tactual  : [%s]\n\texpected: [%s]" % (email.subject, expected_subject))
        self.assertTrue(email.content.__len__() > 0, "Content not set!")

    def test_create_popularity(self):
        input_movies = [
            MovieItem("t1", 12.344),
            MovieItem("t2", 9.39),
            MovieItem("t3", 0.555)
        ]
        input_movies[0].rating = 4.4
        input_movies[1].rating = 5.5
        input_movies[2].rating = 6.6

        email = self.mail_gen.create_email(input_movies)

        expected = test_email_content.splitlines(True)
        actual = email.content.splitlines(True)

        diff = difflib.unified_diff(expected, actual)
        diff_msg = ''.join(diff)

        self.assertTrue(diff_msg.__len__() == 0, "Content differs: \n%s" % diff_msg)


test_email_content = open("resources/test_mail_content.html").read()
