# Python playground

## JSON + Email - Movie release checker

Checks dvd releases from [http://api.nytimes.com](http://api.nytimes.com), adds data fetched with
[http://imdbpy.sourceforge.net](http://imdbpy.sourceforge.net) and sends an email with the results.

### Run requirements
Email account setting required in a shell script called `drc_variables.sh` in the root folder.

`drc_variables.sh` template:

```shell
#!/bin/bash

export set DRC_SMTP_SERVER="your_server:port"
export set DRC_SENDER="your_sender_email_address"
export set DRC_DESTINATION="your_destination_email_address"

export set DRC_USERNAME="your_server_username"
export set DRC_PASSWORD="your_server_password"

export set DRC_TIMES_API_KEY="your_ny_times_api_key"
```

#### Start app

Execute script `run_movie_release_check.sh` which requires the file `drc_variables.sh` to be created.
No further parameters required.


### Test requirements
Tests also need to be executed with at least the environment variable `DRC_TIMES_API_KEY` set to a real API key.
