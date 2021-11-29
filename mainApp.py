from tkinter import *

import changeData
from queries import *

import login
import menu
import order
import orderChoose
import dishRestriction
import addDishInOrder
import addCook
import addWaiter
import setCookActivity
import setWaiterActivity
import changeDish
import addDishInMenu
import deleteDish
import productList
import setDishOrderStatuss
import addAmountProduct
import addProduct
import showTotalSum
import popularDishes
import popularProducts
import allWorkers
import changeProduct

def mainApp(entryUserId):
    window = Tk()
    window.title("Restaurant Database")
    window.geometry('420x600')
    window.resizable(False, False)
    window['background'] = 'light pink'
    flagId = FALSE

    print(entryUserId, "    ?")

    font_header = ('Times New Roman', 15, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11, 'bold')
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

            creds_label = Label(window, text='Welcome, Cook!', font=font_header, justify=CENTER, **header_padding,
                                background="light pink", foreground="dark blue")
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

            creds_label = Label(window, text='Welcome, Waiter!', font=font_header, justify=CENTER, **header_padding,
                                background="light pink", foreground="dark blue")
            creds_label.grid(column=2, row=2)

        connection_to_db.close()
        return flag

    flagId = FALSE

    def checkForDirector(idUser):
        directorMode = FALSE
        if (getUserId(idUser) == 5):
            directorMode = TRUE
            creds_label = Label(window, text='Welcome, Director!', font=font_header, justify=CENTER, **header_padding,
                                background="light pink", foreground="dark blue")
            creds_label.grid(column=2, row=2)
            low_label = Label(window, text='---', font=font_header,  **header_padding,
                                background="light pink", foreground="dark blue")
            low_label.grid(column=2, row=19)
        return directorMode

    def getTotalPeriodSum(minDate, maxDate):
        getPeriodSum(maxDate, minDate)

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

    flagId = getTypeOfUser(entryUserId)
    tired = entryUserId

    def getTotalPrice(idOrder):
        getTotalSum(idOrder)

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

    def clickedDishRestriction():
        window.destroy()
        dishRestriction.dishRestriction(getUserId(tired))

    def clickedAddDishInOrder():
        window.destroy()
        addDishInOrder.addDishInOrder(getUserId(tired))

    def clickedAddCook():
        window.destroy()
        addCook.addCook(getUserId(tired))

    def clickedAddWaiter():
        window.destroy()
        addWaiter.addWaiter(getUserId(tired))

    def clickedSetCookActivity():
        window.destroy()
        setCookActivity.setCookActivity(getUserId(tired))

    def clickedSetWaiterActivity():
        window.destroy()
        setWaiterActivity.setWaiterActivity(getUserId(tired))

    def clickedUpdateDish():
        window.destroy()
        changeDish.updateDish(getUserId(tired))

    def clickedAddDishInMenu():
        window.destroy()
        addDishInMenu.addDishInMenu(getUserId(tired))

    def clickedDeleteDish():
        window.destroy()
        deleteDish.deleteDish(getUserId(tired))

    def clickedProduct():
        window.destroy()
        productList.productList(getUserId(tired))

    def clickedDishOrderStatus():
        window.destroy()
        setDishOrderStatuss.setDishOrderStatuss(getUserId(tired))

    def clickedAddAmountProduct():
        window.destroy()
        addAmountProduct.addAmountProduct(getUserId(tired))

    def clickedGetTotal():
        idOrder = IdOrder_entry.get()
        getTotalPrice(idOrder)

    def clickedAddProduct():
        window.destroy()
        addProduct.addProductInList(getUserId(tired))

    def clickedGetPeriodSum():
        minDate = minday_entry.get()
        maxDate = maxday_entry.get()
        res = getPeriodSum(maxDate, minDate)
        print(res)
        window.destroy()
        showTotalSum.showTotalSum(getUserId(tired), res)

    def clickedPopularDushes():
        window.destroy()
        popularDishes.popularDishes(getUserId(tired))

    def clickedPopularProducts():
        window.destroy()
        popularProducts.popularProducts(getUserId(tired))

    def clickedAllWorkers():
        window.destroy()
        allWorkers.allWorker(getUserId(tired))

    def clickedChangeProduct():
        window.destroy()
        changeProduct.changeProduct(getUserId(tired))


    directorMode = checkForDirector(entryUserId)

    print(entryUserId, '    eto id')
    print(directorMode, '    eto mode')

    if (directorMode == TRUE):
        cook_label = Label(window, text='Cooks block', font=label_font, justify=LEFT, **header_padding,
                            background="light pink", foreground="dark red")
        cook_label.grid(column=1, row=3)

        waiter_label = Label(window, text='Waiters block', font=label_font, justify=RIGHT, **header_padding,
                            background="light pink", foreground="dark red")
        waiter_label.grid(column=3, row=3)

        waiter_label = Label(window, text='Menu block', font=label_font, justify=CENTER, **header_padding,
                             background="light pink", foreground="dark red")
        waiter_label.grid(column=2, row=3)

        change1_data_btn = Button(window, text='Change data', command=clickedChangeData, font=button_font, foreground='blue')
        change1_data_btn.grid(column=3, row=6)

        change2_data_btn = Button(window, text='Change data', command=clickedChangeData, font=button_font,
                                  foreground='blue')
        change2_data_btn.grid(column=1, row=6)

        addcook_btn = Button(window, text='Add cook', command=clickedAddCook, font=button_font, foreground='blue')
        addcook_btn.grid(column=1, row=4)

        menu_btn = Button(window, text='Check menu', command=clickedMenu, font=button_font, foreground='blue')
        menu_btn.grid(column=2, row=8)

        order_btn = Button(window, text='Check order', command=clickedOrderChoose, font=button_font, foreground='blue')
        order_btn.grid(column=2, row=4)

        lo_btn = Button(window, text='Log out', command=clickedLogout, font=button_font, foreground='blue')
        lo_btn.grid(column=2, row=20)

        addwaiter_btn = Button(window, text='Add waiter', command=clickedAddWaiter, font=button_font, foreground='blue')
        addwaiter_btn.grid(column=3, row=4)

        setcookstatus_btn = Button(window, text='SetCookStatus', command=clickedSetCookActivity, font=button_font, foreground='blue')
        setcookstatus_btn.grid(column=1, row=5)

        setwaiter_btn = Button(window, text='SetWaiterStatus', command=clickedSetWaiterActivity, font=button_font,
                                   foreground='blue')
        setwaiter_btn.grid(column=3, row=5)

        updatedish_btn = Button(window, text='Update dish', command=clickedUpdateDish, font=button_font,
                                   foreground='blue')
        updatedish_btn.grid(column=2, row=7)

        adddish_btn = Button(window, text='Add dish', command=clickedAddDishInMenu, font=button_font,
                                foreground='blue')
        adddish_btn.grid(column=2, row=5)

        deletedish_btn = Button(window, text='Delete dish', command=clickedDeleteDish, font=button_font,
                             foreground='blue')
        deletedish_btn.grid(column=2, row=6)

        deletedish_btn = Button(window, text='Check products', command=clickedProduct, font=button_font,
                                foreground='blue')
        deletedish_btn.grid(column=2, row=9)

        order_btn = Button(window, text='Add product', command=clickedAddProduct, font=button_font, foreground='blue')
        order_btn.grid(column=2, row=10)

        maxday_label = Label(window, text='Max day', font=label_font, justify=RIGHT, **header_padding,
                             background="light pink", foreground="dark red")
        maxday_label.grid(column=2, row=15)

        maxday_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
        maxday_entry.grid(column=2, row=16)

        minday_label = Label(window, text='Min day', font=label_font, justify=RIGHT, **header_padding,
                             background="light pink", foreground="dark red")
        minday_label.grid(column=2, row=13)

        minday_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
        minday_entry.grid(column=2, row=14)

        period_btn = Button(window, text='get total period sum', command=clickedGetPeriodSum, font=button_font, foreground='blue')
        period_btn.grid(column=2, row=17)

        views_label = Label(window, text='Views block', font=label_font, justify=RIGHT, **header_padding,
                             background="light pink", foreground="dark red")
        views_label.grid(column=3, row=7)

        views_label = Label(window, text='Others block', font=label_font, justify=RIGHT, **header_padding,
                             background="light pink", foreground="dark red")
        views_label.grid(column=1, row=7)

        popdish_btn = Button(window, text='All workers', command=clickedAllWorkers, font=button_font,
                             foreground='blue')
        popdish_btn.grid(column=1, row=8)

        popdish_btn = Button(window, text='Update product', command=clickedChangeProduct, font=button_font,
                             foreground='blue')
        popdish_btn.grid(column=1, row=9)

        popdish_btn = Button(window, text='Pop dishes', command=clickedPopularDushes, font=button_font,
                            foreground='blue')
        popdish_btn.grid(column=3, row=8)

        popprod_btn = Button(window, text='Pop prod', command=clickedPopularProducts, font=button_font,
                             foreground='blue')
        popprod_btn.grid(column=3, row=9)


    if (directorMode == FALSE):
        # cook
        if (flagId == TRUE):
            menu_btn = Button(window, text='Check menu', command=clickedMenu, font=button_font, foreground='blue')
            menu_btn.grid(column=2, row=3)

            order_btn = Button(window, text='Check order', command=clickedOrderChoose, font=button_font, foreground='blue')
            order_btn.grid(column=3, row=3)

            lo_btn = Button(window, text='Log out', command=clickedLogout, font=button_font, foreground='blue')
            lo_btn.grid(column=1, row=3)

            od_btn = Button(window, text='Set orderdesc status', command=clickedDishOrderStatus, font=button_font, foreground='blue')
            od_btn.grid(column=1, row=4)

            products_btn = Button(window, text='Check products', command=clickedProduct, font=button_font,
                                    foreground='blue')
            products_btn.grid(column=2, row=4)

            deletedish_btn = Button(window, text='add Amount', command=clickedAddAmountProduct, font=button_font,
                                    foreground='blue')
            deletedish_btn.grid(column=3, row=4)

        # waiter
        if (flagId == FALSE):
            menu_btn = Button(window, text='Check menu', command=clickedMenu, font=button_font, foreground='blue')
            menu_btn.grid(column=2, row=3)

            add_btn = Button(window, text='Add dish in order', command=clickedAddDishInOrder, font=button_font, foreground='blue')
            add_btn.grid(column=3, row=3)

            order_btn = Button(window, text='Check order', command=clickedOrderChoose, font=button_font, foreground='blue')
            order_btn.grid(column=1, row=4)

            dishr_btn = Button(window, text='Update dish', command=clickedDishRestriction, font=button_font,
                           foreground='blue')
            dishr_btn.grid(column=2, row=4)

            lo_btn = Button(window, text='Log out', command=clickedLogout, font=button_font, foreground='blue')
            lo_btn.grid(column=1, row=3)

            cook_label = Label(window, text='Enter Order to sum', font=label_font, justify=LEFT, **header_padding,
                               background="light pink", foreground="dark red")
            cook_label.grid(column=3, row=4)

            IdOrder_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
            IdOrder_entry.grid(column=3, row=5)



            entrr_btn = Button(window, text='Enter', command=clickedGetTotal, font=button_font, foreground='green')
            entrr_btn.grid(column=3, row=6)


    window.mainloop()
