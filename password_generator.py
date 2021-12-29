import random
import string

def password_generator(number_of_characters=15):
    # Defining characters to generate the password from
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list("!@#$%&*()+^")

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


"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator")
number_of_letters = int(input(f"How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

letters_list = [random.choice(letters) for i in range(0, number_of_letters)]
numbers_list = [random.choice(numbers) for i in range(0, number_of_numbers)]
symbols_list = [random.choice(symbols) for i in range(0, number_of_symbols)]
combined_list = letters_list + numbers_list + symbols_list

random.shuffle(combined_list)
password = "".join(combined_list)
#password = "".join(random.shuffle(letters_list + numbers_list + symbols_list))
print(letters_list)
print(numbers_list)
print(symbols_list)
print(password)


def password_generator(number_of_characters=15):
    characters_list = letters + numbers + symbols
    random_generated_list = [random.choice(characters_list) for i in range(0, number_of_characters)]
    joined_characters_list = "".join(random_generated_list)
    password = f"{joined_characters_list[:5]}-{joined_characters_list[5:10]}-{joined_characters_list[10:15]}"
    return passwor
new_password = password_generator()
print(new_password)
"""
