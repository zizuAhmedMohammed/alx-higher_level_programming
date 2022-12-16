#!/usr/bin/python3
"""scrept that return header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
