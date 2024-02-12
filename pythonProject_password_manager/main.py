from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    pass_box.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_number + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_box.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_box.get()
    mail_user = mail_user_box.get()
    password = pass_box.get()
    new_data={
        website: {
            "email": mail_user,
            "password": password,
       }
    }
    if website and mail_user and password:
        yes_no = messagebox.askyesno(title=website,
                                     message=f"These are the details entered:\nEmail: {mail_user}\nPassword: {password}\n Save?")
        if yes_no:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_box.delete(0, END)
                pass_box.delete(0, END)
    else:
        messagebox.showwarning(title="Alert!",message="Please write in every box!")

#Find password

def find_pass():
    website = website_box.get()
    with open("data.json") as file:
        data = json.load(file)
        print(data)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")





# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)
website_label=Label(text="Website")
website_label.grid(column=0,row=1)
mail_user_label=Label(text="Email/Username")
mail_user_label.grid(column=0,row=2)
pass_label=Label(text="Password")
pass_label.grid(column=0,row=3)
generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=42,command=save_pass)
add_button.grid(column=1,row=4,columnspan=2)
website_box=Entry(width=24)
website_box.grid(column=1,row=1)
mail_user_box=Entry(width=42)
mail_user_box.insert(0,"eduardscutariu@yahoo.com")
mail_user_box.grid(column=1,row=2,columnspan=2)
pass_box=Entry(width=24)
pass_box.grid(column=1,row=3)
search_button = Button(text="Search",command=find_pass,width=15)
search_button.grid(column=2,row=1)



window.mainloop()