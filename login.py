from tkinter import *
from tkinter import messagebox

from pyodbc import Row

from mainApp import *
from queries import *
import changePassword
import forgotPassword

def logInForm():
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

    main_label = Label(window, text='Restaurant Database', font=font_header, justify=CENTER, **header_padding)
    main_label['background'] = 'white'
    main_label.pack()
    username_label = Label(window, text='Name', font=label_font, **base_padding)
    username_label['background'] = 'white'
    username_label.pack()

    def clicked():
        username = username_entry.get()
        password = password_entry.get()

        if getLogin(username) and (getPassword(username, password)):
            window.destroy()
            mainApp(getUserIdWithLogin(username))
        else:
            wrong_creds_label = Label(window, text='Wrong creds', font=font_header, justify=CENTER, **header_padding)
            wrong_creds_label['background'] = 'white'
            wrong_creds_label.pack()
        print(username, password)
        print(getLogin(username))

    def clickedChangePassword():
        username = username_entry.get()
        window.destroy()
        changePassword.changePassword(getUserIdWithLogin(username))

    def clickedForgot():
        username = username_entry.get()
        window.destroy()
        forgotPassword.forgotPassword(getUserIdWithLogin(username), username)

    # поле ввода имени
    username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка для поля ввода пароля
    password_label = Label(window, text='Password', font=label_font, **base_padding)
    password_label['background'] = 'white'
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(window, bg='#fff', fg='#444', show='*', font=font_entry)
    password_entry.pack()
    # кнопка отправки формы
    send_btn = Button(window, text='Enter', command=clicked, font=button_font, foreground='green')
    send_btn.pack(**base_padding)

    change_btn = Button(window, text='Change', command=clickedChangePassword, font=button_font, foreground='green')
    change_btn.pack(**base_padding)

    #forgot_btn = Button(window, text='Forgot', command=clickedForgot, font=button_font, foreground='green')
    #forgot_btn.pack(**base_padding)

    window.mainloop()