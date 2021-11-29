from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def popularProducts(EntryUserId):
    window = Tk()
    window.title('popularProducts')
    window.geometry('500x280')
    window.resizable(False, False)
    window['background'] = 'light pink'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId

    popularProdList = getPopularProducts()
    rowCount = 4


    def clickedBack():
            window.destroy()
            mainApp.mainApp(getUserId(tired))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.grid(column=3, row=2)

    mainprice_label = Label(window, text='Name/Amount', font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
    mainprice_label.grid(column=2, row=3)


    for i  in range(10):
        price_label = Label(window, text=popularProdList[i], font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
        price_label.grid(column=2, row=rowCount)
        rowCount += 1

    window.mainloop()