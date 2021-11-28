from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *

def deleteDish(EntryUserId):
    window = Tk()
    window.title('changeData')
    window.geometry('200x320')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    def clickedEnter():
        idDish = iddish_entry.get()

        deleteDishFromMenu(idDish)
        window.destroy()
        mainApp.mainApp(getUserId(EntryUserId))


    iddish_label = Label(window, text='Id dish', font=label_font, **base_padding)
    iddish_label['background'] = 'white'
    iddish_label.pack()

    # поле ввода iddish
    iddish_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    iddish_entry.pack()

    # кнопка отправки формы
    send_btn = Button(window, text='Enter', command=clickedEnter, font=button_font, foreground='green')
    send_btn.pack(**base_padding)

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(EntryUserId))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.pack()

    window.mainloop()