#!/bin/bash
# This line tells the computer that this script should be executed using the Bash shell.
#
# Script:               301 Ops Challenge 4
# Author:               Kevin Hoang
# Purpose:              To create a bash script that alters file permissions of everything in a directory   
# Resources:            https://chat.openai.com/share/19e67a71-9413-47ff-a4b9-69ba81169506
#                       https://superuser.com/questions/1181091/ping-using-local-lookback-ip

                        


# Start of the Bash script

while true; do
    # Start of the outer loop (runs indefinitely until broken)
    while true; do
        # Start of the inner loop (displays the menu repeatedly)
        clear
        # Clears the terminal screen for a clean display
        echo "Menu:"
        echo "1. Hello World"
        echo "2. Ping Self"
        echo "3. IP Info"
        echo "4. User Input"
        echo "5. Exit"
        # Prints the menu options

        read -p "Enter your choice: " choice
        # Prompts the user to enter their choice and stores it in the variable 'choice'

        case $choice in
            # Start of the case statement, evaluates the user's choice
            1)
                # Case for option 1 (Hello World)
                echo "Hello World!"
                ;;
            2)
                # Case for option 2 (Ping Self)
                ping -I 127.0.0.1 127.0.0.1
                ;;
            3)
                # Case for option 3 (IP Info)
                echo "Network Adapter Information:"
                ip a
                ;;
            4)
                # Case for option 4 (User Input)
                read -p "Enter some information: " user_input
                # Prompts the user to enter information and stores it in 'user_input'

                # Conditional statement to evaluate user input
                if [[ "$user_input" == "example" ]]; then
                    # If the user entered "example"
                    echo "You entered 'example'. Performing some action based on the input."
                    # Custom action can be added here
                else
                    # If the user entered something else
                    echo "You entered: $user_input"
                fi
                ;;
            5)
                # Case for option 5 (Exit)
                read -p "Are you sure you want to exit? (y/n): " confirm_exit
                # Prompts the user to confirm exit and stores the choice in 'confirm_exit'

                if [ "$confirm_exit" == "y" ]; then
                    # If the user confirmed ('y'), exit the script
                    echo "Exiting..."
                    exit 0
                else
                    # If the user chose not to exit ('n')
                    echo "Cancelled exit."
                fi
                ;;
            *)
                # Default case if the user entered an invalid option
                echo "Invalid option. Please enter a valid choice."
                ;;
        esac
        # End of the case statement

        read -p "Press enter to continue..."
        # Prompts the user to press Enter to continue to the next iteration
    done
    # End of the inner loop
done
# End of the outer loop

