# Python

# Script Name:                  Ops Challenge: Bash in Python
# Author:                       Kevin Hoang
# Date of latest revision:      12/04/2023
# Purpose:                      Ensures consistency and adherence to the Python naming conventions. 
# Execution:                    OpsChallenge06.py
# Resource:                     https://chat.openai.com/share/bd8ae187-a9fe-4e88-847b-b1e798d3086d

# Import the 'os' module
import os

# Declare and initialize variables
variable1 = "GySgtCPD"
variable2 = 50
variable3 = True

# Print the variables
print("variable 1:", variable1)
print("variable 2:", variable2)
print("variable 3:", variable3)

# Execute bash commands using the 'os' module
# Command 1: whoami
whoami_result = os.popen("whoami").read()
print("UserLogIn: \n", whoami_result)

ip_result = os.popen("ip a").read()
print("IP addresses: \n", ip_result)

# Command 3: lshw -short
lshw_result = os.popen("sudo lshw -short").read()
print("Hardware information:\n", lshw_result)