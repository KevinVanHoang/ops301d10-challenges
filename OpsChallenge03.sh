#!/bin/bash
# This line tells the computer that this script should be executed using the Bash shell.
#
# Script:               301 Ops Challenge 3
# Author:               Kevin Hoang
# Purpose:              To create a bash script that alters file permissions of everything in a directory    
# Resources:            https://chat.openai.com/share/e8cd2b57-8e03-432b-9958-504e619d2dd1    


# Print the current working directory
echo "Current working directory: $(pwd)"

# Start a loop that keeps going until we say to stop
while true; do
    # Ask the user to type the path of a folder
    read -p "Please Enter Path: " directory_path

    # Check if what the user typed is a real folder
    echo "Attempting to enter folder: $directory_path"
    if [ -d "$directory_path" ]; then
        # If it's a real folder, tell the user it's okay
        echo "Yay! You entered a real folder: $directory_path"

        # Start another loop for asking the user for a number
        while true; do
            # Ask the user to type a number for permissions (like 777)
            read -p "Please Enter Permissions Number (e.g., 777): " permissions

            # Check if the number is in the right format (like 777)
            if [[ $permissions =~ ^[0-7]{3}$ ]]; then
                # If it's the right format, tell the user it's a good number
                echo "Awesome! You entered a good number: $permissions"

                # Go inside the folder the user told us earlier
                cd "$directory_path" || exit 1

                # Change the permissions of all the files in that folder
                find . -type f -exec chmod "$permissions" {} +

                # Tell the user that we changed the permissions
                echo "We changed the permissions for all the files in the folder!"

                # Show the user a list of all the files and their permissions
                ls -la

                # Break out of the loop because we're done
                break
            else
                # If the number is not in the right format, tell the user to try again
                echo "Oops! That's not a valid number. Please enter a three-digit number (e.g., 777)."
            fi
        done

        # Break out of the outer loop because we're done
        break
    else
        # If the folder is not real, tell the user to try again
        echo "Uh-oh! That's not a real folder. Please try again."
    fi
done

