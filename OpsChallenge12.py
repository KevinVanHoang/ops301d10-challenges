# Python

# Script Name:                  Ops Challenge: Python Requests Library
# Author:                       Kevin Hoang
# Date of latest revision:      12/12/2023
# Purpose:                      Python script performing HTTP GET requests using the requests Python library.
# Execution:                    OpsChallenge12.py
# Resources:                    https://github.com/KevinVanHoang/seattle-ops-301d10/blob/main/class-12/challenges/DEMO.md
#                               https://realpython.com/python-requests/
#                               https://chat.openai.com/c/fb5fd6a9-39a7-41e9-853d-41f53623f4ee

import requests  # Import the requests library for making HTTP requests

# Dictionary mapping HTTP status codes to plain terms
status_codes_mapping = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error',
}

# Function to translate status codes
def translate_status_code(status_code):
    return status_codes_mapping.get(status_code, f'Unknown Status Code: {status_code}')

# Prompt the user for a destination URL
address = input("Type in a destination URL (format: google.com):\n")

# Check if the input already contains 'https://' or 'http://'
if not address.startswith('https://') and not address.startswith('http://'):
    user_url = 'https://' + address
else:
    user_url = address

# Ask for HTTP method choice
valid_methods = ['get', 'post', 'put', 'delete', 'head', 'patch', 'options']

choice = input("\nSelect an HTTP method from the following list:\n" + '\n'.join(valid_methods) + "\n").lower()

while choice not in valid_methods:
    print("Invalid choice. Please select a valid HTTP method.")
    choice = input().lower()

# Display the entire request and ask for confirmation
print("\nYou are about to send the following request:")
print(f"URL: {user_url}")
print(f"HTTP Method: {choice.upper()}")

confirmation = input("\nDo you want to proceed? (yes/no): ").lower()

if confirmation == 'yes':
    # Perform the HTTP request using the requests library
    response = requests.request(choice.upper(), user_url)
    
    # Translate the status code and print the response status code and content
    translated_status = translate_status_code(response.status_code)
    print(f"\nResponse Status Code: {translated_status}")
    
    # Print response headers
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    print("\nResponse Content:")
    print(response.text)
else:
    print("Request canceled.")
