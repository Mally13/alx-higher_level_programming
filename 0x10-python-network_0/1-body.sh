#!/bin/bash
# Displays body of a response
if [ $(curl -s -o /dev/null -w '%{http_code}' $1) -eq 200 ]; then
	echo "$(curl -s "$1")"
fi
