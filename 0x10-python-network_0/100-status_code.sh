#!/bin/bash
# Sends a request to a URL, and displays the status code received
curl -s -o /dev/null -w '%{http_code}' "$1"
