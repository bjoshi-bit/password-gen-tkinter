from tkinter import *
import random

generated_password = ''
everything = ''
symbols = """~`!@#$%^&*()_-+={[}]|:;"'<,>./?"""
numbers = '1234567890'
chars = 'abcdefghijklmnopqrstuvwxyz'
upperchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

root = Tk()
root.title('Password Generator')
root.geometry("300x300")
password = Label(text='')


def generation():
    global generated_password
    generated_password = ''
    copied.config(text='')

    checker()
    for i in range(length_var.get()):
        ran = random.choice(everything)
        generated_password += ran
    password.config(text=generated_password)
    copy.grid(column=0, row=8, columnspan=1)


def copy():
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    copied.config(text='Copied!', fg='green')
    copied.grid(column=0)


def checker():
    global everything
    everything = ''

    if length_var.get() > 20:
        length_var.set(20)

    if uchar_var.get() == 1:
        everything += upperchars
    if char_var.get() == 1:
        everything += chars
    if num_var.get() == 1:
        everything += numbers
    if sym_var.get() == 1:
        everything += symbols


generate = Button(text='Generate Password', command=generation)
copy = Button(text='Copy', command=copy)
copied = Label(text='Copied!', fg='green')
sym_var = IntVar()
check_symbols = Checkbutton(text='Symbols? Ex. @$%}', variable=sym_var)
check_symbols.select()
num_var = IntVar()
check_numbers = Checkbutton(text='Numbers? Ex. 1234', variable=num_var)
check_numbers.select()
char_var = IntVar()
check_chars = Checkbutton(text='Lowercase? Ex. abcd', variable=char_var)
check_chars.select()
uchar_var = IntVar()
check_upperchars = Checkbutton(text='Uppercase? Ex. ABCD', variable=uchar_var)
check_upperchars.select()
length_var = IntVar()
Label(text='Length (8-20):').grid(column=1, row=0)
Spinbox(root, from_=8, to=20, textvariable=length_var).grid(column=1, row=1, sticky=S)

check_upperchars.grid(column=0, row=0, sticky=W)
check_chars.grid(column=0, row=1, sticky=W)
check_numbers.grid(column=0, row=2, sticky=W)
check_symbols.grid(column=0, row=3, sticky=W)
password.grid(column=0, row=9, rowspan=2)
generate.grid(column=1, row=3)


root.resizable(False, False)
root.mainloop()
