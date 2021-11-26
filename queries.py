import pyodbc

def getCooksNames():
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
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
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
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
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT login from Users where login ='{login}'")
    ifLogin = cursor.fetchone()
    connection_to_db.close()

    return ifLogin

def getPassword(password):
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()
    cursor.execute(f"SELECT login from Users where password ='{password}'")
    ifPassword = cursor.fetchone()
    connection_to_db.close()

    return ifPassword

def getUserIdWithLogin(login):
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
    cursor = connection_to_db.cursor()

    cursor.execute(f"SELECT IdUser from Users where login ='{login}'")
    ifIdUser = cursor.fetchone().IdUser
    connection_to_db.close()

    return ifIdUser

def getUserId(id):
    connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-PI2BET6;Database=rest;Trusted_Connection=yes;')
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
        menuName.append(row.Name)
    connection_to_db.close()
    return menuName



