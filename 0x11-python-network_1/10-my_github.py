#!/usr/bin/python3
"""in this task:
- uses the GitHub API to display your id
- takes your GitHub credentials (username and password)
"""
import sys
import requests


if __name__ == "__main__":    
    r = requests.get("https://api.github.com/user", auth = (sys.argv[1], sys.argv[2]))
    print(r.json().get("id"))
