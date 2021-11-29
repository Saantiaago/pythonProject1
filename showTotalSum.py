from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def showTotalSum(EntryUserId, res):
    window = Tk()
    window.title('dishRestriction')
    window.geometry('170x500')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId

    description_label = Label(window, text=res, font=label_font, **base_padding)
    description_label['background'] = 'white'
    description_label.pack()

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(EntryUserId))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.pack()

    window.mainloop()