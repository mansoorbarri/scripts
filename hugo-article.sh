#!/bin/bash

# Check if folder name is provided
if [ $# -eq 0 ]; then
    echo "Usage: ./create_files.sh folder_name"
    exit 1
fi

# Get the folder name from command line argument
name=$1

# Create the default file
hugo new articles/2024/${name}/${name}.md

# Create the Urdu (ur) version of the file
hugo new articles/2024/${name}/${name}.ur.md
