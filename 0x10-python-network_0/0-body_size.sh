#!/bin/bash
# Displays the size of the body of the response
size=$(curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r')
echo "$size"
