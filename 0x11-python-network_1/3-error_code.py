#!/usr/bin/python3
""" this script
- sends a request to the URL and urllib, request, error, HTTPError
- displays the body of the response,sys
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as respons:
            print(respons.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
