#!/bin/bash

# Script:               301 Ops Challenge 2 
# Author:               Kevin Hoang
# Purpose:              To create a script to copy /var/log/syslog to working directory        
# Resources:            https://chat.openai.com/share/e06018e0-9746-4323-9363-a53145dbb1c8    


# Set the source file path
source_file="/var/log/syslog"  

# Get the current date and time
current_datetime=$(date +"%Y%m%d_%H%M%S")

# Set the destination file path with the appended date and time
destination_file="syslog_$current_datetime.log"

# Copy the syslog file to the current working directory with the new filename
cp "$source_file" "$destination_file"

echo "Copied $source_file to $destination_file"
