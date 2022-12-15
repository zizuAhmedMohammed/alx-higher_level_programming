#!/bin/bash
# sends DELETE req to URL and display the body of the response.
curl -s "$1" -X DELETE
