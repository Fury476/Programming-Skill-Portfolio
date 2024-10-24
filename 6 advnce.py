# Define the correct password
correct_password = "password123"

# Set the maximum number of attempts
max_attempts = 5

# Loop for up to max_attempts
for attempt in range(max_attempts):
    user_input = input("Please enter the password: ")
    
    if user_input == correct_password:
        print("Access granted!")
        break #break the loop
    else:
        remaining_attempts = max_attempts - (attempt + 1)
        print("Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
else:
    print("Maximum attempts reached. The User have been alerted ⚠️2.")
