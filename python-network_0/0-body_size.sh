#!/bin/bash

size=$(curl -s -o /dev/null -w '%{size_download}' "$1")
