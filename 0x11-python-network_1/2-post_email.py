#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
