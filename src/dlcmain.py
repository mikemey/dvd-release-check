import logging

import mailsender
from moviereleases import MovieReleases, create_email
from tmdburl import urls

# set up logging:

logging.addLevelName(logging.WARNING, "WARN")
logging.basicConfig(format='%(asctime)s %(levelname)5s - %(message)s')
logging.getLogger("dlc").setLevel(logging.INFO)
logger = logging.getLogger("dlc")

releases = MovieReleases(urls['search_releases'])
data = releases.last_weeks_releases()

if "error" in data:
    logger.warn("exiting!")
    exit(1)

email = create_email(data)
mailsender.send(email.subject, email.content)

logger.info("finished.")
exit()
