from tkinter import *

import changeData
from queries import *

import login
import menu
import order
import orderChoose

def mainApp(EntryUserId):
    window = Tk()
    window.title("Restaurant Database")
    window.geometry('320x200')
    window.resizable(False, False)
    window['background'] = 'light pink'
    flagId = FALSE

    print(EntryUserId, "    ?")

    font_header = ('Times New Roman', 15, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    # def cookChosen(event):
    #   lbl = Label(window, text=comboCooks.get())
    #   lbl.grid(column=1, row=0)

    # def waiterChosen(event):
    #    lbl = Label(window, text=comboWaiters.get())
    #    lbl.grid(column=1, row=1)

    def getTypeOfUser(idd):

        connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
        cursor2 = connection_to_db.cursor()
        cursor2.execute(f"SELECT Cooks.IdCook from Cooks  where Cooks.IdUser ='{idd}' ")
        flag = TRUE
        if (cursor2.fetchone()) is not None:
            connection_to_db.close()

            connection_to_db = pyodbc.connect(
                r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
            cursor2 = connection_to_db.cursor()
            cursor2.execute(f"SELECT Cooks.IdCook from Cooks  where Cooks.IdUser ='{idd}' ")

            idFlag = cursor2.fetchone().IdCook
            flag = TRUE

            creds_label = Label(window, text='Welcome, Cook!', font=font_header, justify=CENTER, **header_padding, background = "light pink", foreground = "dark blue")
            creds_label.grid(column=2, row=2)

        connection_to_db.close()
        connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
        cursor1 = connection_to_db.cursor()
        cursor1.execute(f"SELECT IdWaiter from Waiters  where Waiters.IdUser ='{idd}' ")

        if (cursor1.fetchone()) is not None:
            connection_to_db.close()

            connection_to_db = pyodbc.connect(
                r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
            cursor1 = connection_to_db.cursor()
            cursor1.execute(f"SELECT IdWaiter from Waiters  where Waiters.IdUser ='{idd}' ")

            idFlag = cursor1.fetchone().IdWaiter
            flag = FALSE

            creds_label = Label(window, text='Welcome, Waiter!', font=font_header, justify=CENTER, **header_padding, background = "light pink", foreground = "light blue")
            creds_label.grid(column=2, row=2)

        connection_to_db.close()
        return flag

    # comboCooks = Combobox(window)
    # comboCooks['state'] = 'readonly'
    # comboCooks.set("Choose cook")
    # comboCooks['values'] = (getCooksNames())
    # comboCooks.grid(column=0, row=0)

    #  comboWaiters = Combobox(window)
    # comboWaiters['state'] = 'readonly'
    # comboWaiters.set("Choose waiter")
    #  comboWaiters['values'] = (getWaitersNames())
    # comboWaiters.grid(column=0, row=1)

    # comboCooks.bind('<<ComboboxSelected>>', cookChosen)
    # comboWaiters.bind('<<ComboboxSelected>>', waiterChosen)

    flagId = getTypeOfUser(EntryUserId)
    tired = EntryUserId

    def clickedMenu():
        window.destroy()
        menu.menu(getUserId(tired))

    def clickedLogout():
        window.destroy()
        login.logInForm()

    def clickedChangeData():
        window.destroy()
        changeData.changeData(getUserId(tired), flagId)

    def clickedOrderChoose():
        window.destroy()
        orderChoose.orderChoose(getUserId(tired))

    lo_btn = Button(window, text='Log out', command=clickedLogout, font=button_font, foreground='blue')
    lo_btn.grid(column=1, row=3)

    menu_btn = Button(window, text='Check menu', command=clickedMenu, font=button_font, foreground='blue')
    menu_btn.grid(column=2, row=3)

    change_data_btn = Button(window, text='Change data', command=clickedChangeData, font=button_font, foreground='blue')
    change_data_btn.grid(column=3, row=3)

    order_btn = Button(window, text='Check order', command=clickedOrderChoose, font=button_font, foreground='blue')
    order_btn.grid(column=1, row=4)

    window.mainloop()



