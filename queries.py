import pyodbc
import bcrypt

key = b'$2b$12$COnvlB9Kses3CthyxNl9pu'


def getCooksNames():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute('Select Name, DateOfBirth, PhoneNumber, mail, Status from Cooks')

    cookName = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        cookName.append(row.Name)
    connection_to_db.close()

    return cookName


def getWaitersNames():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute('Select Name, DateOfBirth, PhoneNumber, mail, Status from Waiters')
    waitersName = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        waitersName.append(row.Name)
    connection_to_db.close()

    return waitersName


def getLogin(login):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT login from Users where login ='{login}'")
    ifLogin = cursor.fetchone().login

    print(ifLogin, '-----')

    connection_to_db.close()

    return ifLogin


def getPassword(login, password):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT password from Users where login ='{login}'")

    ifPass = str.encode(cursor.fetchone().password)
    password = bcrypt.hashpw(str.encode(password), key)

    print(ifPass, '   ', password)

    if ifPass == password:
        return ifPass

    connection_to_db.close()

    return False


def changePassword(login, password):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    password = bcrypt.hashpw(str.encode(password), key)
    cursor.execute(f"UPDATE Users Set password = '{password.decode()}' where login ='{login}'")
    connection_to_db.commit()


def getUserIdWithLogin(login):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT IdUser from Users where login ='{login}'")
    ifIdUser = cursor.fetchone().IdUser
    connection_to_db.close()

    return ifIdUser


def getUserId(id):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT IdUser from Users where IdUser ='{id}'")
    ifIdUser = cursor.fetchone().IdUser
    connection_to_db.close()

    return ifIdUser


def getMenuList():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description, Price from Menu")

    menuName = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        menuName.append(row)
    connection_to_db.close()
    return menuName


def getMenuListName():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description, Price from Menu")

    menuName = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        menuName.append(row.Name)
    connection_to_db.close()
    return menuName


def getMenuListDescription():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description, Price from Menu")

    menuName = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        menuName.append(row.Description)
    connection_to_db.close()
    return menuName


def getMenuListPrice():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description, Price from Menu")

    menuName = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        menuName.append(row.Price)
    connection_to_db.close()
    return menuName


def getAmountOfMenu():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description, Price from Menu")

    amount = -2

    menuName = []
    while 1:
        amount += 1
        row = cursor.fetchone()

        if not row:
            break
        menuName.append(row)
    connection_to_db.close()

    return amount


def updateDataCooks(idUser, name, dateofbirth, newPhoneNumber, newMail):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"UPDATE Cooks SET Name = '{name}', DateOfBirth = '{dateofbirth}', PhoneNumber = '{newPhoneNumber}'"
                   f", Mail = '{newMail}' where IdUser = '{idUser}' ")

    connection_to_db.commit()


def updateDataWaiters(idUser, name, dateofbirth, newPhoneNumber, newMail):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"UPDATE Waiters SET Name = '{name}', DateOfBirth = '{dateofbirth}', PhoneNumber = '{newPhoneNumber}'"
        f", Mail = '{newMail}' where IdUser = '{idUser}' ")

    connection_to_db.commit()


def getOrder(idOrder):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"Select Distinct WorkOrder.*, Menu.Name as Dishes, Menu.Price as Price, OrderDescription.AmountOfDish "
        f"as Amount from WorkOrder, Waiters, ProductDescription, OrderDescription, Menu, ProductList, Cooks where "
        f"WorkOrder.IdWaiter = Waiters.IdWaiter and WorkOrder.IdOrder = ProductDescription.OrderId and ProductDescription.IdProduct "
        f"= ProductList.IdProduct and WorkOrder.IdOrder = OrderDescription.OrderId and OrderDescription.IdDish = "
        f"Menu.IdDish and WorkOrder.IdOrder ='{idOrder}'")
    ifOrder = cursor.fetchone()
    connection_to_db.close()

    return ifOrder


def getOrderId(idOrder):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT WorkOrder.IdOrder from WorkOrder where WorkOrder.IdOrder ='{idOrder}'")
    ifIdOrder = cursor.fetchone().IdOrder
    connection_to_db.close()

    return ifIdOrder


def getIdDish(idDish):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT Menu.IdDish from Menu where Menu.IdDish ='{idDish}'")
    ifIdDish = cursor.fetchone().IdDish
    connection_to_db.close()

    return ifIdDish


def getIdDishWithName(Name):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT Menu.IdDish from Menu where Menu.Name ='{Name}'")
    ifIdDish = cursor.fetchone().IdDish
    connection_to_db.close()

    return ifIdDish


def updateDishStatus(Name, status):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"Update Menu Set Status = '{status}' Where Name = '{Name}'")

    connection_to_db.commit()


def insertDishInOrder(idOrderDescription, orderId, amountOfDish, status, idDish, idCook):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"INSERT INTO OrderDescription (IdOrderDescription, OrderId, AmountOfDish, Status, IdDish, IdCook) VALUES ('{idOrderDescription}', '{orderId}', '{amountOfDish}', '{status}', '{idDish}', '{idCook}');")

    connection_to_db.commit()


def registerCook(IdUser, login, password, IdCook, name, dateOfBirth, phoneNumber, mail, status):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    newpassword = bcrypt.hashpw(str.encode(password), key)
    cursor.execute(
        f"INSERT INTO Users (IdUser, login, password) VALUES ('{IdUser}', '{login}', '{password}') "
        f"INSERT INTO Waiters(IdWaiter, IdUser, Name, DateOfBirth, PhoneNumber, Mail, Status) "
        f"VALUES ('{IdCook}', '{IdUser}', '{name}', '{dateOfBirth}', '{phoneNumber}', '{mail}', '{status}')"
        f"UPDATE Users Set password = '{newpassword.decode()}' where login ='{login}'")

    connection_to_db.commit()


def registerWaiter(IdUser, login, password, IdCook, name, dateOfBirth, phoneNumber, mail, status):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    newpassword = bcrypt.hashpw(str.encode(password), key)
    cursor.execute(
        f"INSERT INTO Users (IdUser, login, password) VALUES ('{IdUser}', '{login}', '{password}') "
        f"INSERT INTO Waiters(IdWaiter, IdUser, Name, DateOfBirth, PhoneNumber, Mail, Status) "
        f"VALUES ('{IdCook}', '{IdUser}', '{name}', '{dateOfBirth}', '{phoneNumber}', '{mail}', '{status}')"
        f"UPDATE Users Set password = '{newpassword.decode()}' where login ='{login}'")

    connection_to_db.commit()


def setCookStatus(idUser, status):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"UPDATE Cooks SET status = '{status}' where IdUser = '{idUser}' ")

    connection_to_db.commit()


def setWaiterStatus(idUser, status):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"UPDATE Waiters SET status = '{status}' where IdUser = '{idUser}' ")

    connection_to_db.commit()


def updateDishDescription(Name, Description, Price):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"Update Menu Set Name = '{Name}', Description = '{Description}', Price = '{Price}' Where Name = '{Name}'")

    connection_to_db.commit()


def setDishInMenu(IdDish, Name, Description, Price, Status):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"INSERT INTO Menu (IdDish, Name, Description, Price, Status) VALUES ('{IdDish}', '{Name}', '{Description}', '{Price}', '{Status}')")

    connection_to_db.commit()


def deleteDishFromMenu(idDish):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"Update OrderDescription Set OrderDescription.IdDish = 100 where OrderDescription.IdDish = '{idDish}' delete from Menu where IdDish = '{idDish}'")

    connection_to_db.commit()

def getProductListName():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description from ProductList")

    productName = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        productName.append(row.Name)
    connection_to_db.close()
    return productName


def getProductListDescription():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description from ProductList")

    productDescription = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        productDescription.append(row.Description)
    connection_to_db.close()
    return productDescription


def getProductListPrice():
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT Name, Description from ProductList")

    productPrice = []
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        productPrice.append(row.Price)
    connection_to_db.close()
    return productPrice

def setDishOrderStatus(idOrderDescription, status):
    connection_to_db = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(
        f"UPDATE OrderDescription SET status = '{status}' where IdOrderDescription = '{idOrderDescription}' ")

    connection_to_db.commit()