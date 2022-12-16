#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    r = requests.get(url)
    commit = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
