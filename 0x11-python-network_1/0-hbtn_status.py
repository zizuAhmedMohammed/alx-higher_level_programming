#!/usr/bin/python3
"""
script that use the package urllib and fetches url
and show body of the response
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    response = response.read()
print('Body response:')
print(f"\t- type: {type(response)}")
print(f"\t- content: {response}")
print(f"\t- utf8 content: {response.decode('utf-8')}")
