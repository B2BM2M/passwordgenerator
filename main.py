from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '\\', '|', ':',
               ';', '"', "'", '<', '>', ',', '.', '?', '/']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    # print(password_list)

    password = "".join(password_list)
    # print(password)
    password_input.insert(0, password)
    pyperclip.copy(password) # saved and paste in your own OS

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_url = website_input.get()
    user_parameter = email_username_input.get()
    user_password = password_input.get()
    store_data = f"\n{website_url} | {user_parameter} | {user_password}"

    if len(website_url)  <= 0 or len(user_parameter)  <= 0 or len(user_password)  <= 0:
        messagebox.showwarning(title="Oops", message="Fields cannot be empty, try again!")
    else:
        is_ok = messagebox.askokcancel(title=website_url, message=f"These are the details entered: \nEmail: {user_parameter} \nPassword: {user_password} \nIs it okay to save?")
        if is_ok:
            with open("password_storage.txt", "a") as file:
                file.write(store_data)
                website_input.delete(0, END)
                #email_username_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

#Create window

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas= Canvas(width=200, height=200, highlightthickness=0)

security_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=security_image)
canvas.grid(column=1, row=0)

#----------------------- Labels ------------------------------------------- #
website = Label(text="Website:")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

#----------------------- Entries ------------------------------------------- #
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()



email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "youremail@gmail.com")

password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)

#----------------------- Buttons ------------------------------------------- #

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
