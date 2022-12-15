#!/bin/bash
# you can use the -H command-line option and pass the header name and value in "Key: Value" format.
curl -sH "X-School-User-Id: 98" "$1"
