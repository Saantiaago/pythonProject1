from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def order(EntryUserId, idOrder):
    window = Tk()
    window.title('Order')
    window.geometry('900x500')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId

    order = getOrder(idOrder)
    #orderId = getOrderIdOrder(idOrder)
    #orderNum = getOrderOrderNumber(idOrder)
    #orderDate = getOrderDate(idOrder)
    #orderIdw = getOrderIdWaiter(idOrder)
    #orderTp = getOrderTotalPrice(idOrder)

    def clickedBack():
            window.destroy()
            mainApp.mainApp(getUserId(tired))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.grid(column=4, row=3)
    main_label = Label(window,
                       text="Order Id/ Order Number / Date /Id Waiter. Total Price / Dishes/ Price of dish / Amount of dish ",
                       font=font_header, justify=CENTER, **header_padding)
    main_label.grid(column=10, row=4)

    rowCount = 5

    for i in range(getAmountOfOrder(idOrder)-1):
        main_label = Label(window, text=order[i], font=font_header, justify=CENTER, **header_padding)
        main_label.grid(column=10, row=rowCount)
       # main_label = Label(window, text=orderNum[i], font=font_header, justify=CENTER, **header_padding)
        #main_label.grid(column=11, row=rowCount)
        #main_label = Label(window, text=orderDate[i], font=font_header, justify=CENTER, **header_padding)
        #main_label.grid(column=12, row=rowCount)
        #main_label = Label(window, text=orderIdw[i], font=font_header, justify=CENTER, **header_padding)
        #main_label.grid(column=13, row=rowCount)
        #main_label = Label(window, text=orderTp[i], font=font_header, justify=CENTER, **header_padding)
        #main_label.grid(column=14, row=rowCount)
        rowCount += 1


    window.mainloop()