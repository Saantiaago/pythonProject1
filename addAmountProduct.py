from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def addAmountProduct(EntryUserId):
    window = Tk()
    window.title('add amount of product')
    window.geometry('900x500')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId


    def clickedEnter():
        idProductDescription = iduser_entry.get()
        amount = getAmountOfProduct(idProductDescription)
        if (amount == None):
            window.destroy()
            mainApp.mainApp(getUserId(tired))
        newAmount = amount_entry.get()
        totalAmount = int(amount) + int(newAmount)
        addAmountOfProduct(idProductDescription, totalAmount)
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(tired))



    menu_btn = Button(window, text='Enter', command=clickedEnter, font=button_font, foreground='green')
    menu_btn.grid(column=4, row=8)

    back_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='red')
    back_btn.grid(column=4, row=10)

    iduser_label = Label(window, text='Name', font=label_font, **base_padding)
    iduser_label['background'] = 'white'
    iduser_label.grid(column=4, row=4)

    # поле ввода имени
    iduser_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    iduser_entry.grid(column=4, row=5)

    amount_label = Label(window, text='Amount to add', font=label_font, **base_padding)
    amount_label['background'] = 'white'
    amount_label.grid(column=4, row=6)

    # поле ввода status
    amount_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    amount_entry.grid(column=4, row=7)

    window.mainloop()