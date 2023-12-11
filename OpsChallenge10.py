# Python

# Script Name:                  Ops Challenge: Python File Handling
# Author:                       Kevin Hoang
# Date of latest revision:      12/08/2023
# Purpose:                      Python script with  file handling capabilities to open and manipulate an existing file
# Execution:                    OpsChallenge10.py
# Resources:                    https://chat.openai.com/share/fa08c592-51cd-4b7b-86b8-0fbdcbc67837
#                               https://www.w3schools.com/python/python_file_open.asp
#                               https://github.com/codefellows/seattle-ops-301d10/tree/main/class-10/challenges



# Import the 'os' module, which provides a way to interact with the operating system
import os

# Set the file path variable to 'example.txt'
file_path = 'example.txt'

# Step 1: Create a new text file
# Open the file in 'write' mode ('w') and use the 'with' statement to ensure proper file handling
with open(file_path, 'w') as file:
    # Write three lines of text to the file
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

# Step 2: Check if the file exists before reading and printing the first line
if os.path.exists(file_path):
    # Open the file in 'read' mode ('r') using the 'with' statement
    with open(file_path, 'r') as file:
        # Read the first line of the file
        first_line = file.readline()
        # Print the first line to the screen
        print("First line:", first_line)
else:
    # Print a message if the file does not exist
    print(f"The file '{file_path}' does not exist.")

# Step 3: Delete the text file if it exists
if os.path.exists(file_path):
    # Use the 'os.remove()' function to delete the file
    os.remove(file_path)
    # Print a message indicating that the file was deleted
    print(f"{file_path} deleted.")
else:
    # Print a message if the file does not exist
    print(f"The file '{file_path}' does not exist.")
