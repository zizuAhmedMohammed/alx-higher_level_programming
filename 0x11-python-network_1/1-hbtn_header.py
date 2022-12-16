#!/usr/bin/python3
"""A script that:
- You must use the packages urllib and sys
- You are not allow to import packages other than urllib and sys
-script that use the package urllib and sys.
-fetches url and show body of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
