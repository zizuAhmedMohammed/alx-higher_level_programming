#!/usr/bin/python3
""" The letter must be sent in the variable q
-If no argument is given, set q=""
-If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
-Otherwise:
-Display Not a valid JSON if the JSON is invalid
-Display No result if the JSON is empty
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parameter = {'q': sys.argv[1] }
    else:
        parameter = {'q': '' }

    url = 'http://0.0.0.0:5000/search_user'
    R = requests.post(url, data = parameter )
    try:
        response = R.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")

    except ValueError:
        print("Not a valid JSON")
