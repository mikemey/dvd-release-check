import mailsender
from moviereleases import MovieReleases, create_email
from mlc_commons import urls, logger

# set up logging:

releases = MovieReleases(urls['search_releases'])
data = releases.last_weeks_releases()

if "error" in data:
    logger.warn("exiting!")
    exit(1)

email = create_email(data)
mailsender.send(email.subject, email.content)

logger.info("finished.")
exit()
