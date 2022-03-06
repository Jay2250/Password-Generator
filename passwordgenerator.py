from tkinter import *

master = Tk()
master.title("Password Generator")


# Method or Algorithm to Generate Password
from random import choice

letters = [chr(i) for i in range(35,125)]
#print(letters)

def GeneratePswd():
    #result = password.generate()
    password = ''
    for i in range(0,9):
        password = password + choice(letters) 
    pswd.insert(0, password)
    
def clear():
    pswd.delete(0,END)
    
    
label1 = Label(master, text='Password Generator', font=('Helvetica',15,'bold'))
pswd = Entry(master)
pswd_generate_button = Button(master, text="Generate", command=GeneratePswd)
clear_button = Button(master, text='Clear', command=clear)

label1.grid(row=1, column=0, columnspan=3)
pswd.grid(row=3, column=1)
pswd_generate_button.grid(row=4, column=1)
clear_button.grid(row=5, column=1)

master.mainloop()
