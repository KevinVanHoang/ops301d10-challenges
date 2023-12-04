#!/bin/bash
# This line tells the computer that this script should be executed using the Bash shell.
#
# Script:               301 Ops Challenge 5
# Author:               Kevin Hoang
# Purpose:              To create a bash script that alters file permissions of everything in a directory   
# Resources:            https://chat.openai.com/share/01a6229f-4080-4730-a4e6-972b1347fd7b
#                       https://www.geeksforgeeks.org/shell-script-to-measure-size-of-a-file/


# Function to generate a timestamp in the format -YYYYMMDDHHMMSS
generate_timestamp() {
    date +"-%Y%m%d%H%M%S"
}

# Function to clear the contents of a log file
clear_log_file() {
    local log_file="$1"
    > "$log_file"  # Redirect an empty output to truncate the file
}

# Function to print file size
print_file_size() {
    local file="$1"
    local size=$(stat -c%s "$file")
    echo "The size of $file is $size Bytes"
}

# path to the file
filepath="/home/amninder/Downloads/cn.zip"

# function to check if a file is a log file
is_log_file() {
    local file="$1"
    # Check if the file has a ".log" extension
    [[ "$file" == *.log ]]
}

# storing file size of the original log file in a variable.
original_size=$(stat -c%s "$filepath")

# check if the file is a log file before displaying size
if is_log_file "$filepath"; then
    echo "The size of log file is $original_size Bytes"
    
    # Clear the contents of the log file
    clear_log_file "$filepath"
    echo "Log file contents cleared."
    
    # Compress the log file
    gzip -c "$filepath" > "$filepath.gz"
    compressed_file="$filepath.gz"
    echo "Log file compressed to $compressed_file"
    
    # Print the size of the compressed file
    print_file_size "$compressed_file"
    
    # Compare the sizes
    compressed_size=$(stat -c%s "$compressed_file")
    echo "Comparison: Original Size: $original_size Bytes, Compressed Size: $compressed_size Bytes"
else
    echo "The file is not a log file. Size is $original_size Bytes"
fi
