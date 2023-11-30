#!/bin/bash
# Displays the size of the body of the response
echo "$(curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r')"
