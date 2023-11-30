#!/bin/bash
# Displays body of a response
status_code=$(curl -s -o /dev/null -w '%{http_code}' $1)
if [ $status_code -eq 200 ]; then
	echo "$(curl -s "$1")"
fi
