from tkinter.ttk import Combobox
from tkinter import *

from queries import *

def mainApp(EntryUserId):
    window = Tk()
    window.title("Restaurant Database")
    window.geometry('800x500')
    window.resizable(False, False)
    window['background'] = 'white'
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

            creds_label = Label(window, text=' Cook!', font=font_header, justify=CENTER, **header_padding)
            creds_label.grid(column=2, row=1)

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

            creds_label = Label(window, text=' Waiter!', font=font_header, justify=CENTER, **header_padding)
            creds_label.grid(column=2, row=1)

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

    def clicked():
        window.destroy()
        menu(getUserId(tired))

    if flagId == TRUE:
        menu_btn = Button(window, text='Check menu', command=clicked, font=button_font, foreground='green')
        menu_btn.grid(column=4, row=3)

    window.mainloop()




def menu(EntryUserId):
    window = Tk()
    window.title('Menu')
    window.geometry('450x250')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 15, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId

    getMenuList()

    def clickedBack():
            window.destroy()
            mainApp(getUserId(tired))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.grid(column=4, row=3)

    window.mainloop()