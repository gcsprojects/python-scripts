# Simple script that generates random passwords
# Takes input from the user on how long the password should be
# And how many passwords to generate


import random
import string

# Get the information we need from the user
num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("How long should they be? "))

# Set the counter to zero
# This ensures the correct number of passwords are generated later
counter = 0

# Define the allowable characters to put into each password
components = [string.ascii_letters, string.digits, "!@#$%&"]
chars = []
for clist in components:
	for item in clist:
		chars.append(item)

# Function to generate the password by randomnly
# getting a character from out allowed list and join them all together
# until we reach the desired password length we got from the user
def generate_password():
	password = []

	for i in range(password_length):
		rchar = random.choice(chars)
		password .append(rchar)
	return "".join(password)

# Finally, we print the passwords to the screen....
print(f"Generating {num_passwords} Passwords...\n")
print("\n")

print("-"*password_length)
while counter <= num_passwords:
	print(generate_password())
	counter = counter + 1
print("-"*password_length)
