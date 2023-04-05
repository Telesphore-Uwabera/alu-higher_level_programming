#!/bin/bash
#Send request and get the size of the response body in bytes
size=$(curl -s -o /dev/null -w '%{size_download}' "$1")
