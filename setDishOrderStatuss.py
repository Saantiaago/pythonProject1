from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def setDishOrderStatuss(EntryUserId):
    window = Tk()
    window.title('set dish order description status')
    window.geometry('500x500')
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
        Name = idorderdesc_entry.get()
        OrderNumber = idordernumber_entry.get()
        status = status_entry.get()
        setDishOrderStatus(Name, OrderNumber, status)
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(tired))



    menu_btn = Button(window, text='Enter', command=clickedEnter, font=button_font, foreground='green')
    menu_btn.grid(column=4, row=11)

    back_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    back_btn.grid(column=4, row=10)

    iduser_label = Label(window, text='OrderNumber', font=label_font, **base_padding)
    iduser_label['background'] = 'white'
    iduser_label.grid(column=4, row=4)

    # поле ввода имени
    idorderdesc_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    idorderdesc_entry.grid(column=4, row=5)

    iduser_label = Label(window, text='Name of dish', font=label_font, **base_padding)
    iduser_label['background'] = 'white'
    iduser_label.grid(column=4, row=6)

    # поле ввода имени
    idordernumber_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    idordernumber_entry.grid(column=4, row=7)

    status_label = Label(window, text='Status', font=label_font, **base_padding)
    status_label['background'] = 'white'
    status_label.grid(column=4, row=8)

    # поле ввода status
    status_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    status_entry.grid(column=4, row=9)

    window.mainloop()