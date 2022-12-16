#!/usr/bin/python3
"""A  script that:
- The email must be sent in the variable email
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    r = requests.post(url, data=value)
    print(f"Your email is: {r.text}")
