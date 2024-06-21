#!/bin/bash

# Check if the token argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <token>"
    exit 1
fi

# Token provided as argument
token="$1"

# Loop through telegraf_0 to telegraf_5
for i in {0..5}
do
  # Define the path to telegraf.conf
  conf_file="./telegraf_$i/telegraf.conf"

  # Check if the conf file exists
  if [ -f "$conf_file" ]; then
    # Replace the token in telegraf.conf
    sed -i "s/token = \"[^\"]*\"/token = \"$token\"/" "$conf_file"
    echo "Token replaced in $conf_file"
  else
    echo "Error: $conf_file does not exist"
  fi
done

echo "Token replacement completed for all telegraf.conf files"

