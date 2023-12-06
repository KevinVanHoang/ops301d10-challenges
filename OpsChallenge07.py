# Python

# Script Name:                  Ops Challenge: Directory Creation
# Author:                       Kevin Hoang
# Date of latest revision:      12/05/2023
# Purpose:                      Python script that generates all directories, sub-directories and files for a user-provided directory path. 
# Execution:                    OpsChallenge07.py
# Resource:                     https://chat.openai.com/share/6249e011-cfc0-4bf1-9780-7cb174777b91
#                               https://www.w3schools.com/python/ref_os_fwalk.asp



# Import the 'os' module
import os

def process_directory(user_input_path):
    # Validate if the provided path exists
    if not os.path.exists(user_input_path):
        print("Invalid path. Please provide a valid directory path.")
        return

    for root, dirs, files in os.walk(user_input_path):
        # Your logic for processing files and directories goes here
        for file in files:
            file_path = os.path.join(root, file)
            print("Processing file:", file_path)

        # You can modify `dirs` to exclude certain directories from being traversed
        # For example, to exclude the 'exclude_dir' directory:
        if 'exclude_dir' in dirs:
            dirs.remove('exclude_dir')

# Get user input for the directory path
user_input_path = input("Enter the directory path: ")

# Call the function with the user-inputted path
process_directory(user_input_path)
