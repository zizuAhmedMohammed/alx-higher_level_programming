#!/usr/bin/python3
"""
A script that:
-script that use the package urllib and sys.
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
