from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def setCookActivity(EntryUserId):
    window = Tk()
    window.title('dishRestriction')
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
        idUser = iduser_entry.get()
        status = status_entry.get()
        setCookStatus(idUser, status)
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(tired))



    menu_btn = Button(window, text='Enter', command=clickedEnter, font=button_font, foreground='green')
    menu_btn.grid(column=4, row=3)

    back_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    back_btn.grid(column=4, row=2)

    iduser_label = Label(window, text='id of user', font=label_font, **base_padding)
    iduser_label['background'] = 'white'
    iduser_label.grid(column=4, row=4)

    # поле ввода имени
    iduser_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    iduser_entry.grid(column=4, row=5)

    status_label = Label(window, text='Status', font=label_font, **base_padding)
    status_label['background'] = 'white'
    status_label.grid(column=4, row=6)

    # поле ввода status
    status_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    status_entry.grid(column=4, row=7)

    window.mainloop()