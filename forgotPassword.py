from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import login
from mainApp import *
from queries import *
import setPassword


def forgotPassword(EntryUserId, username1):
    window = Tk()
    window.title('Auth')
    window.geometry('350x350')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 15, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    main_label = Label(window, text='Enter login', font=font_header, justify=CENTER, **header_padding)
    main_label['background'] = 'white'
    main_label.pack()
    username_label = Label(window, text='Name', font=label_font, **base_padding)
    username_label['background'] = 'white'
    username_label.pack()

    def clicked():
        username = username_entry.get()
        password = getOnlyPassword(username)
        print(password, '   this is password')
        window.destroy()
        login.logInForm()


    username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # кнопка отправки формы
    send_btn = Button(window, text='Enter', command=clicked, font=button_font, foreground='green')
    send_btn.pack(**base_padding)

    window.mainloop()