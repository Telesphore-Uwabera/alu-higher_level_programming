#!/usr/bin/python3

size=$(curl -s -o /dev/null -w '%{size_download}' "$1")
