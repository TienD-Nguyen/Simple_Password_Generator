# This file is dedicated for a simple password generator with for-loop and without randomisation of characters' position
# Also, the user can declare how many letters, numbers and special characters they want in their password

import random

# Declare lists of printable character that can be used for password.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Intro to the file
print("Welcome to the PyPassword Generator")

# Asking input from the user and convert the answer into integer data type.
number_of_letters = int(input(f"How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

# Create lists of random chosen characters
letters_list = [random.choice(letters) for i in range(0, number_of_letters)]
numbers_list = [random.choice(numbers) for i in range(0, number_of_numbers)]
symbols_list = [random.choice(symbols) for i in range(0, number_of_symbols)]

# Combining lists into one single list and joining all elements inside a newly created list to generate a password
combined_list = letters_list + numbers_list + symbols_list
password = "".join(combined_list)

# Printing password to the console.
print(letters_list)
print(numbers_list)
print(symbols_list)
print(password)
