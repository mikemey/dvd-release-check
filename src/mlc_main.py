import mail_sender
from movie_releases import MovieReleases, create_email
from mlc_commons import urls, logger

# set up logging:

releases = MovieReleases(urls['search_releases'])
movies = releases.last_weeks_releases()

if "error" in movies:
    logger.warn("exiting!")
    exit(1)

print movies

email = create_email(movies)
mail_sender.send(email.subject, email.content)

logger.info("finished.")
exit()
