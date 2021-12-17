from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def addCook(EntryUserId):
    window = Tk()
    window.title('dishRestriction')
    window.geometry('170x800')
    window.resizable(False, False)
    window['background'] = 'light pink'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId


    def clickedEnter():
        idUser = 0
        login = login_entry.get()
        password = password_entry.get()
        idCook = 0
        name = name_entry.get()
        dateOfBirth = bday_entry.get()
        phoneNumber = phone_entry.get()
        mail = mail_entry.get()
        status = status_entry.get()

        registerCook(idUser, login, password, idCook, name, dateOfBirth, phoneNumber, mail, status)
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(tired))



    login_label = Label(window, text='Login of user', font=label_font, **base_padding, foreground='dark blue', background="light pink")
    login_label['background'] = 'light pink'
    login_label.grid(column=4, row=3)

    # поле ввода login
    login_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    login_entry.grid(column=4, row=4)

    password_label = Label(window, text='Password of user', font=label_font, **base_padding, foreground='dark blue', background="light pink")
    password_label['background'] = 'light pink'
    password_label.grid(column=4, row=5)

    # поле ввода password
    password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    password_entry.grid(column=4, row=6)


    name_label = Label(window, text='Name', font=label_font, **base_padding, foreground='dark blue', background="light pink")
    name_label['background'] = 'light pink'
    name_label.grid(column=4, row=9)

    # поле ввода имени
    name_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    name_entry.grid(column=4, row=10)

    bday_label = Label(window, text='Birthday date', font=label_font, **base_padding, foreground='dark blue', background="light pink")
    bday_label['background'] = 'light pink'
    bday_label.grid(column=4, row=11)

    # поле ввода bday
    bday_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    bday_entry.grid(column=4, row=12)

    phone_label = Label(window, text='Phone', font=label_font, **base_padding, foreground='dark blue', background="light pink")
    phone_label['background'] = 'light pink'
    phone_label.grid(column=4, row=13)

    # поле ввода phone
    phone_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    phone_entry.grid(column=4, row=14)

    mail_label = Label(window, text='Mail', font=label_font, **base_padding, foreground='dark blue', background="light pink")
    mail_label['background'] = 'light pink'
    mail_label.grid(column=4, row=15)

    # поле ввода mail
    mail_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    mail_entry.grid(column=4, row=16)

    status_label = Label(window, text='Status', font=label_font, **base_padding, foreground='dark blue', background="light pink")
    status_label['background'] = 'light pink'
    status_label.grid(column=4, row=17)

    # поле ввода status
    status_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    status_entry.grid(column=4, row=18)

    back_btn = Button(window, text='back', command=clickedBack, font=button_font, foreground='red')
    back_btn.grid(column=4, row=19)

    enter_btn = Button(window, text='enter', command=clickedEnter, font=button_font, foreground='green')
    enter_btn.grid(column=4, row=20)

    window.mainloop()