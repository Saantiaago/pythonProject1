from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def dishRestriction(EntryUserId):
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


    def clickedBack():
        idDish = dish_entry.get()
        status = status_entry.get()
        updateDishStatus(idDish, status)
        window.destroy()
        mainApp.mainApp(getUserId(tired))



    menu_btn = Button(window, text='enter', command=clickedBack, font=button_font, foreground='green')
    menu_btn.grid(column=4, row=3)

    dish_label = Label(window, text='Id of dish', font=label_font, **base_padding)
    dish_label['background'] = 'white'
    dish_label.grid(column=4, row=4)

    # поле ввода имени
    dish_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    dish_entry.grid(column=4, row=5)

    status_label = Label(window, text='Status', font=label_font, **base_padding)
    status_label['background'] = 'white'
    status_label.grid(column=4, row=6)

    # поле ввода имени
    status_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    status_entry.grid(column=4, row=7)

    window.mainloop()