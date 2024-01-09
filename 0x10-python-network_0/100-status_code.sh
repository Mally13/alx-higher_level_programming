#!/bin/bash
# Displays the status code of a response
curl -I -w "%{http_code}" "$1"
