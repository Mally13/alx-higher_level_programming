#!/usr/bin/env bash
# Displays the size of the body of the response

url="$1"
response_size=$(curl -sI "$url" | awk '/Content-Length/ {print $2}' | tr -d '\r')
if [ -n "$response_size" ]; then
	echo "$response_size"
fi
