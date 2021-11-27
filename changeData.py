from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *

def changeData(EntryUserId, flagId):
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
        name = name_entry.get()
        datebday = datebday_entry.get()
        phone = phone_entry.get()
        mail = mail_entry.get()
        if (flagId == TRUE):
            updateDataCooks(getUserId(EntryUserId), name, datebday, phone, mail)
        else:
            updateDataWaiters(getUserId(EntryUserId), name, datebday, phone, mail)
        window.destroy()
        mainApp.mainApp(getUserId(EntryUserId))


    username_label = Label(window, text='Name', font=label_font, **base_padding)
    username_label['background'] = 'white'
    username_label.pack()

    # поле ввода имени
    name_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    name_entry.pack()

    bday_label = Label(window, text='Birthday date', font=label_font, **base_padding)
    bday_label['background'] = 'white'
    bday_label.pack()

    # поле ввода др
    datebday_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    datebday_entry.pack()

    phone_label = Label(window, text='Phone', font=label_font, **base_padding)
    phone_label['background'] = 'white'
    phone_label.pack()

    # поле ввода телефона
    phone_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    phone_entry.pack()

    mail_label = Label(window, text='Mail', font=label_font, **base_padding)
    mail_label['background'] = 'white'
    mail_label.pack()

    mail_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    mail_entry.pack()

    # кнопка отправки формы
    send_btn = Button(window, text='Enter', command=clickedEnter, font=button_font, foreground='green')
    send_btn.pack(**base_padding)

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(EntryUserId))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.pack()

    window.mainloop()