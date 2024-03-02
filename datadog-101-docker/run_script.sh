#!/bin/bash
  
# Set the duration for which the script should run in seconds
duration=30

# Path to your Python script
python_script_path="generate_load_script/load.py"

# Run the Python script in the background
python3 "$python_script_path" &

# Get the process ID of the last background command
pid=$!

# Sleep for the specified duration
sleep $duration

# Terminate the background process
kill $pid     