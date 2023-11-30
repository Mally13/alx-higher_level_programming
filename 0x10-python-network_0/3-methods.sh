#!/bin/bash
# Displays server's accepted http methods
echo "$(curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-)"
