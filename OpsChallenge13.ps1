# Define user details
$firstName = "Franz"
$lastName = "Ferdinand"
$username = "ferdi"
$email = "ferdi@GlobeXpower.com"
$department = "TPS"

# Set the password for the new user
$password = ConvertTo-SecureString -AsPlainText "YourPasswordHere" -Force

# Specify the AD OU (Organizational Unit) where you want to create the user
$ouPath = "OU=Users,DC=YourDomain,DC=com"

# Create the new AD user
New-ADUser -SamAccountName $username -UserPrincipalName "$username@YourDomain.com" -GivenName $firstName -Surname $lastName -Name "$firstName $lastName" -EmailAddress $email -Department $department -AccountPassword $password -Enabled $true -Path $ouPath

# Display a message indicating success
Write-Host "User $username created successfully."

# Additional note: Make sure to replace "YourPasswordHere" and "YourDomain" with your actual password and domain information.
