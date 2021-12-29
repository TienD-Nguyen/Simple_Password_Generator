# This file is dedicated for generating password that similar to Apple's style of password suggestion.
# Characters are randomised and chosen from a list of both letters, numbers and special characters.

import random
import string

def password_generator(number_of_characters=15):
    # Defining characters to generate the password from
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list("! @#$%&*()+^")

    # Combining lists of characters
    characters = letters + numbers + symbols

    # Randomised sample characters from the list
    generated_characters = random.sample(characters, number_of_characters)

    # Joining characters in the list and return the password
    temp_password = "".join(generated_characters)
    password = f"{temp_password[:5]}-{temp_password[5:10]}-{temp_password[10:15]}"

    return password

new_password = password_generator()
print(new_password)
