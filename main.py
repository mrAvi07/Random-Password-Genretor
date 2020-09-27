from tkinter import *
import string
import random

root = Tk()
root.title("Password Generator")
root.geometry("400x300")


def passwordgen():

     s1 = string.ascii_uppercase
     s2 = string.ascii_lowercase
     s3 = string.digits
     s4 = ['@', '!', '#', '$', '&', '?']


     sample = []
     sample.extend(s1)
     sample.extend(s2)
     sample.extend(s3)
     sample.extend(s4)

     random.shuffle(sample)

     passget = ("".join(sample[0:(int(new_entry.get()))]))

     new_entry.delete(0, END)

     mylabel = Label(root,
        text=passget,
        padx=30,
        pady=30,
        font=("verdana", "10","bold")
    )
     mylabel.place(x=130, y=250)


mylabel = Label(
    root,
    text="PASSWORD GENERATOR",
    padx=10,
    pady=10,
    bg = "green",
    fg = "white",
    font=("times", "16", "bold")
)
mylabel.place(x=50, y=50)


lab_2 = Label(
    root,
    text="Length of password",
    padx=5,
    pady=5,
    font=("verdana","10")
)
lab_2.place(x=50, y=150)


new_entry = Entry(
    root
)
new_entry.place(x=200, y=150)


btn_2 = Button(
    root,
    text="New password",
    command=passwordgen,
    bg="green",
    fg="white",
    activebackground="black",
    font=("verdana", "10")
)
btn_2.place(x=60, y=200)

btn_1 = Button(
    root,
    text="Close",
    command=quit,
    width="10",
    bg="green",
    fg="white",
    font=("verdana","10")
)
btn_1.place(x=230, y=200)

if __name__=="__main__":
    root.mainloop()
