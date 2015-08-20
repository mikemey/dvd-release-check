# Python playground

## JSON + Email - Movie release checker

Checking last weeks movie releases from The Movie DB.

src folder: `src`
test folder: `test`

Email account setting required in a shell script called `email_variables.sh` in the root folder.

`email_variables.sh` template:

```
#!/bin/bash

export set DRC_SMTP_SERVER="your_server:port"
export set DRC_SENDER="your_sender_email_address"
export set DRC_DESTINATION="your_destination_email_address"

export set DRC_USERNAME="your_server_username"
export set DRC_PASSWORD="your_server_password"

```

# Node + Express server

src folder: `app`

Express server to serve simple json data.
