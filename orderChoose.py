from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import order
import mainApp
from queries import *

def orderChoose(EntryUserId):
    window = Tk()
    window.title('choose order')
    window.geometry('200x25')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId







    def clicked():
        idOrder = orderid_entry.get()
        window.destroy()
        order.order(getUserId(tired), getOrderId(idOrder))
        print(idOrder, "  eto order")

    #order = getOrder(idOrder)

    orderid_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    orderid_entry.grid(column=1, row=1)

    send_btn = Button(window, text='Enter', command=clicked, font=button_font, foreground='blue')
    send_btn.grid(column=2, row=1)

   # def clickedBack():
    #        window.destroy()
    #       mainApp.mainApp(getUserId(tired))

    #menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    #menu_btn.grid(column=4, row=3)

    #main_label = Label(window, text=order, font=font_header, justify=CENTER, **header_padding)
    #main_label.grid(column=10, row=10)

    window.mainloop()