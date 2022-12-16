#!/usr/bin/python3
"""script that fetches url using requests module """
import requests


if __name__ == "__main__":
    r = requests.get("http://0.0.0.0:5050/status")
    R = r.text
    print("Body response:")
    print("\t- type: {}".format(type(R)))
    print("\t- content: {}".format(R))
