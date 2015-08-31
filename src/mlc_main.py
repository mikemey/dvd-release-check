from imdb_lookup import ImdbLookup
from imdb_ratings import ImdbRatings
import mail_sender
from mail_gen import MailGen
from movie_releases import MovieReleases
from mlc_commons import urls, logger

releases = MovieReleases(urls['search_releases'])
mail_gen = MailGen()
enhancer = ImdbRatings(ImdbLookup())

movies = releases.last_weeks_releases()
movies = enhancer.enhance_data(movies)

if "error" in movies:
    logger.warn("exiting!")
    exit(1)

email = mail_gen.create_email(movies)
mail_sender.send(email.subject, email.content)

logger.info("finished.")
exit()
