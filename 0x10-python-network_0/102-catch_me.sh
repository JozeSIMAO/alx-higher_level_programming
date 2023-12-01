#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to get the server response with "You got me!"
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me" -H "Referer: 0.0.0.0:5000/catch_me"
