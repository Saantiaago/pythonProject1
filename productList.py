from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def menu(EntryUserId):
    window = Tk()
    window.title('Menu')
    window.geometry('280x500')
    window.resizable(False, False)
    window['background'] = 'light pink'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId

    nameList = getMenuListName()
    descriptionList = getMenuListDescription()
    priceList = getMenuListPrice()
    rowCount = 4


    def clickedBack():
            window.destroy()
            mainApp.mainApp(getUserId(tired))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.grid(column=3, row=2)
    mainname_label = Label(window, text='Name', font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
    mainname_label.grid(column=5, row=3)
    maindesc_label = Label(window, text='Description', font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
    maindesc_label.grid(column=6, row=3)
    mainprice_label = Label(window, text='Price', font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
    mainprice_label.grid(column=7, row=3)


    for i  in range(getAmountOfMenu()):
        name_label = Label(window, text=nameList[i], font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
        name_label.grid(column=5, row=rowCount)
        description_label = Label(window, text=descriptionList[i], font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
        description_label.grid(column=6, row=rowCount)
        price_label = Label(window, text=priceList[i], font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
        price_label.grid(column=7, row=rowCount)
        rowCount += 1

    window.mainloop()