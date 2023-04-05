#!/bin/bash
# Send GET request using curl and store response body in a variable
response_body=$(curl -s -o /dev/null -w "%{http_code}" $url)
