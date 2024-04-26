#!/bin/bash
# Sends a POST request to a URL, with a json file as the data
curl -s -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"
