#!/bin/bash

# Update package list
sudo apt update

# Install Python 3 and pip3
sudo apt install -y python3 python3-pip

# Install necessary Python libraries
pip3 install requests pydantic
