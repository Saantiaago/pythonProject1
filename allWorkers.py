from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def allWorker(EntryUserId):
    window = Tk()
    window.title('allWorker')
    window.geometry('300x500')
    window.resizable(False, False)
    window['background'] = 'light pink'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId

    popularProdList = getAllWorkers()
    print(popularProdList)
    rowCount = 4
    print(getAmountWorkers())

    def clickedBack():
            window.destroy()
            mainApp.mainApp(getUserId(tired))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.grid(column=3, row=2)

    mainprice_label = Label(window, text='Name', font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
    mainprice_label.grid(column=2, row=3)


    for i  in range(getAmountWorkers()-1):
        price_label = Label(window, text=popularProdList[i], font=font_header, justify=CENTER, **header_padding, foreground='dark blue', background="light pink")
        price_label.grid(column=2, row=rowCount)
        rowCount += 1

    window.mainloop()