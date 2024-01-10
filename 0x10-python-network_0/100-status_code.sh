#!/bin/bash
# Displays only the status code of a response
curl -I -w "%{http_code}" -s -o /dev/null "$1"
