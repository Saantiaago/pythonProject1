from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def addDishInOrder(EntryUserId):
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


    def clickedEnter():
        idOrderDescription = orderdescription_entry.get()
        orderId = orderid_entry.get()
        amountOfDish = amountofdish_entry.get()
        idCook = idcook_entry.get()
        dishName = dish_entry.get()
        idDish = getIdDishWithName(dishName)
        status = status_entry.get()
        insertDishInOrder(idOrderDescription, orderId, amountOfDish, status, idDish, idCook)
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    idorderdesc_label = Label(window, text='Id of Order Description', font=label_font, **base_padding)
    idorderdesc_label['background'] = 'white'
    idorderdesc_label.grid(column=4, row=1)

    # поле ввода idOrderDDesc
    orderdescription_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    orderdescription_entry.grid(column=4, row=2)

    orderid_label = Label(window, text='Id of Order', font=label_font, **base_padding)
    orderid_label['background'] = 'white'
    orderid_label.grid(column=4, row=3)

    # поле ввода orderid
    orderid_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    orderid_entry.grid(column=4, row=4)

    amountofdish_label = Label(window, text='Amount of dish', font=label_font, **base_padding)
    amountofdish_label['background'] = 'white'
    amountofdish_label.grid(column=4, row=5)

    # поле ввода amountofdish
    amountofdish_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    amountofdish_entry.grid(column=4, row=6)

    idcook_label = Label(window, text='Id of cook', font=label_font, **base_padding)
    idcook_label['background'] = 'white'
    idcook_label.grid(column=4, row=7)

    # поле ввода idcook
    idcook_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    idcook_entry.grid(column=4, row=8)


    dish_label = Label(window, text='Name of dish', font=label_font, **base_padding)
    dish_label['background'] = 'white'
    dish_label.grid(column=4, row=9)


    # поле ввода имени
    dish_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    dish_entry.grid(column=4, row=10)

    status_label = Label(window, text='Status', font=label_font, **base_padding)
    status_label['background'] = 'white'
    status_label.grid(column=4, row=11)

    # поле ввода имени
    status_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    status_entry.grid(column=4, row=12)

    back_btn = Button(window, text='back', command=clickedBack, font=button_font, foreground='green')
    back_btn.grid(column=4, row=13)

    enter_btn = Button(window, text='enter', command=clickedEnter, font=button_font, foreground='green')
    enter_btn.grid(column=4, row=14)

    window.mainloop()