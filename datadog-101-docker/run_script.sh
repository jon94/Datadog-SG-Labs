#!/bin/bash
  
# Set the duration for which the script should run in seconds
duration=30

# Path to your Python script
python_script_path="generate_load_script/load.py"

# Calculate the end time
end_time=$((SECONDS + duration))

# Run the Python script in a loop until the specified duration
while [ $SECONDS -lt $end_time ]; do
    # Run the Python script
    python3 "$python_script_path"

    # Sleep for a short interval before running the script again
    sleep 1
done