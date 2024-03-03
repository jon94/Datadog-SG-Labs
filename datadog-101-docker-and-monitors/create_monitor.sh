#!/bin/bash

# Change directory to the create_monitor directory
cd create_monitor

# Iterate through all Python files in the directory
for file in *.py; do
    echo "Running $file"
    python3 "$file"
    echo "Completed $file"
done