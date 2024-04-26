#!/bin/bash
# List the HTTP methods allowed by the server 
curl -s -I "$1" | grep Allow | sed 's/Allow: //'
