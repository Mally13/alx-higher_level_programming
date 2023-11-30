#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays body
curl -s -X DELETE "$1"
