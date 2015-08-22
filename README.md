# Python playground

## JSON + Email - Movie release checker

Checking last weeks movie releases from https://www.themoviedb.org/ and
sends an email with last weeks movie releases.

### Run requirements
Email account setting required in a shell script called `drc_variables.sh` in the root folder.

`drc_variables.sh` template:

```
#!/bin/bash

export set DRC_SMTP_SERVER="your_server:port"
export set DRC_SENDER="your_sender_email_address"
export set DRC_DESTINATION="your_destination_email_address"

export set DRC_USERNAME="your_server_username"
export set DRC_PASSWORD="your_server_password"

export set DRC_MOVIEDB_API_KEY="your_moviedb_api_key"
export set DRC_IMDB_API_KEY="not_yet_implemented"
```

#### Start app

Execute script `run_movie_release_check.sh` which requires the file `drc_variables.sh` to be created.
No further parameters required.


### Test requirements
Tests also need to be executed with at least the environment variable `DRC_MOVIEDB_API_KEY` set to a real API key.


# Node + Express server

src folder: `app`

Express server to serve simple json data.
