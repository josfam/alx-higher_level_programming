#!/bin/bash
# Sends a GET request, and displays the body of the response. Sets a header variable
curl -s -X "GET" -H "X-School-User-Id: 98" "$1"
