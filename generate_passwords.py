#!/usr/bin/env python3

import random
import string

num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("How long should they be? "))
counter = 0
components = [string.ascii_letters, string.digits, "!@#$%&"]

chars = []

for clist in components:
	for item in clist:
		chars.append(item)

def generate_password():
	password = []

	for i in range(password_length):
		rchar = random.choice(chars)
		password .append(rchar)

	return "".join(password)

print(f"Generating {num_passwords} Passwords...\n")
print("\n")

#print("-----Passwords------")
print("-"*password_length)
while counter <= num_passwords:
	print(generate_password())
	counter = counter + 1
print("-"*password_length)

#print("-------End----------")
