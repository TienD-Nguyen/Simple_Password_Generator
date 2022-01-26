from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string
def generate_password():
    # Deleting any previous entered password in the entry
    password_entry.delete(0, END)

    letters = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = list("!@#$%&")

    # Combining lists of characters
    characters = letters + numbers + symbols

    # Randomising sample characters from the list
    generated_characters = random.sample(characters, 15)

    # Joining characters in the list
    temp_password = "".join(generated_characters)
    generated_password = f"{temp_password[:5]}-{temp_password[5:10]}-{temp_password[10:15]}"

    password_entry.insert(0, generated_password)

    # Copy the password onto a clip board
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    entered_website = website_entry.get()
    inserted_password = password_entry.get()
    inserted_username = username_entry.get()

    # Checking whether fields are emptied and prompt a message
    if len(entered_website) == 0 or len(inserted_password) == 0 or len(inserted_username) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave fields empty.")
    else:
        # Prompting message box for user to confirm entered data
        is_ok = messagebox.askokcancel(title=entered_website, message=f"There are the details entered: " 
                                                                      f"\nEmail: {inserted_username} " 
                                                                      f"\nPassword: {inserted_password} " 
                                                                      f"\n Are you ready to proceed?")

        # If conforming, then proceed to saving the password along other fields.
        if is_ok:
            with open("data.txt", "a") as file:
                # Saving password onto an existing/new local file
                file.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)
                username_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas.pack()

lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
username = Label(text="Email/Username:")
username.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry = Entry(width=39)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
