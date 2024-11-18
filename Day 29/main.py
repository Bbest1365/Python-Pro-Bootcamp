from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0,row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)

#Entries
website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)




window.mainloop()









