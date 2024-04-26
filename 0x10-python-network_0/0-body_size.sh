#!/bin/bash
# displays the size of the body of a response from a provided url
curl -s -o /dev/null -w '%{size_download}\n' "$1"
