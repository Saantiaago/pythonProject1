from tkinter import *
from tkinter import messagebox

from pyodbc import Row

from mainApp import *
from queries import *


def setPassword(login, EntryUserId):
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

    main_label = Label(window, text='Enter new pass', font=font_header, justify=CENTER, **header_padding)
    main_label['background'] = 'white'
    main_label.pack()

    def clicked():
        password = password_entry.get()
        changeNewPassword(getLogin(login), password)
        window.destroy()
        mainApp(getUserIdWithLogin(login))

    # метка для поля ввода пароля
    password_label = Label(window, text='new Password', font=label_font, **base_padding)
    password_label['background'] = 'white'
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(window, bg='#fff', fg='#444', show='*', font=font_entry)
    password_entry.pack()
    # кнопка отправки формы
    send_btn = Button(window, text='Enter', command=clicked, font=button_font, foreground='green')
    send_btn.pack(**base_padding)

    window.mainloop()