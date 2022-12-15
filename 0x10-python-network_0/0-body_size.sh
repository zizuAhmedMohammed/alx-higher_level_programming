#!/bin/bash
# sends a request to the input URL and displays the content length of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
