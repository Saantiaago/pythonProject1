from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def addWaiter(EntryUserId):
    window = Tk()
    window.title('dishRestriction')
    window.geometry('170x800')
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
        login = login_entry.get()
        password = password_entry.get()
        idWaiter = idwaiter_entry.get()
        name = name_entry.get()
        dateOfBirth = bday_entry.get()
        phoneNumber = phone_entry.get()
        mail = mail_entry.get()
        status = status_entry.get()

        registerWaiter(idUser, login, password, idWaiter, name, dateOfBirth, phoneNumber, mail, status)
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(tired))


    iduser_label = Label(window, text='Id of User', font=label_font, **base_padding)
    iduser_label['background'] = 'white'
    iduser_label.grid(column=4, row=1)

    # поле ввода idUser
    iduser_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    iduser_entry.grid(column=4, row=2)

    login_label = Label(window, text='Login of user', font=label_font, **base_padding)
    login_label['background'] = 'white'
    login_label.grid(column=4, row=3)

    # поле ввода login
    login_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    login_entry.grid(column=4, row=4)

    password_label = Label(window, text='Password of user', font=label_font, **base_padding)
    password_label['background'] = 'white'
    password_label.grid(column=4, row=5)

    # поле ввода password
    password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    password_entry.grid(column=4, row=6)

    idwaiter_label = Label(window, text='Id of cook', font=label_font, **base_padding)
    idwaiter_label['background'] = 'white'
    idwaiter_label.grid(column=4, row=7)

    # поле ввода idcook
    idwaiter_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    idwaiter_entry.grid(column=4, row=8)

    name_label = Label(window, text='Name', font=label_font, **base_padding)
    name_label['background'] = 'white'
    name_label.grid(column=4, row=9)

    # поле ввода имени
    name_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    name_entry.grid(column=4, row=10)

    bday_label = Label(window, text='Birthday date', font=label_font, **base_padding)
    bday_label['background'] = 'white'
    bday_label.grid(column=4, row=11)

    # поле ввода bday
    bday_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    bday_entry.grid(column=4, row=12)

    phone_label = Label(window, text='Phone', font=label_font, **base_padding)
    phone_label['background'] = 'white'
    phone_label.grid(column=4, row=13)

    # поле ввода phone
    phone_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    phone_entry.grid(column=4, row=14)

    mail_label = Label(window, text='Mail', font=label_font, **base_padding)
    mail_label['background'] = 'white'
    mail_label.grid(column=4, row=15)

    # поле ввода mail
    mail_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    mail_entry.grid(column=4, row=16)

    status_label = Label(window, text='Status', font=label_font, **base_padding)
    status_label['background'] = 'white'
    status_label.grid(column=4, row=17)

    # поле ввода status
    status_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    status_entry.grid(column=4, row=18)

    back_btn = Button(window, text='back', command=clickedBack, font=button_font, foreground='green')
    back_btn.grid(column=4, row=19)

    enter_btn = Button(window, text='enter', command=clickedEnter, font=button_font, foreground='green')
    enter_btn.grid(column=4, row=20)

    window.mainloop()