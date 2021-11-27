--������� �������
Use rest;

SELECT Cooks.IdCook from Users, Cooks  where Users.IdUser = Cooks.IdUser and Users.IdUser =1

SELECT Cooks.IdCook, Waiters.IdWaiter from Users, Cooks, Waiters  where Users.IdUser = Cooks.IdUser and Users.IdUser = Waiters.IdWaiter and Users.IdUser = 3

--1. ��������� ������� ������
declare @currentId int='1', 
		@newName varchar(50)='Alexander Filippov', @newdateOfBirth date='2001-05-02', 
		@newPhoneNumber varchar(15)='8264560780', @newMail varchar(30)='asdfr@yahoo.com';
Update Cooks
	Set Name = @newName, DateOfBirth = @newDateOfBirth, 
		PhoneNumber = @newPhoneNumber, Mail = @newMail
	Where IdCook = @currentId;

--2. ��������� ��� ������� �� ����������
declare @currentId int='1', 
		@newStatus bit ='false';
Update Cooks
	Set Status = @newStatus
	Where IdCook = @currentId;

--3. ��������� ������� ���������
declare @currentId int='1',  
		@newName varchar(50)='aaaaaaaa', @newdateOfBirth date='1999-05-02', 
		@newPhoneNumber varchar(15)='8264560780', @newMail varchar(30)='aaaaa@gmail.com';
Update Waiters
	Set Name = @newName, DateOfBirth = @newDateOfBirth, 
		PhoneNumber = @newPhoneNumber, Mail = @newMail
	Where IdWaiter = @currentId;

--4. ��������� ��� ������� �� ����������
declare @currentId int='1', 
		@newStatus bit ='false';
Update Waiters
	Set Status = @newStatus
	Where IdWaiter = @currentId;

--5. ��������� ��������, ��������, ���� �����
declare @currentName varchar(50)='Och Vkusno', 
		@newPrice money='900', @newDescription varchar(100)='Ooooochen vkusnoe', @newName varchar(50) = 'Ochen Vkusno';
Update Menu
	Set Name = @newName, Description = @newDescription, 
		Price = @newPrice
	Where Name = @currentName;

--6. ��������� ������� �����
declare @currentId int='2', 
		@newStatus bit ='true';
Update Menu
	Set Status = @newStatus
	Where IdDish = @currentId;

--7. ��������� ���������� ���������
declare @currentIdProductDescription varchar(50)='1', 
		@newAmountOfProductInGm int ='777';
Update ProductDescription
	Set AmountOfProductInGm = @newAmountOfProductInGm
	Where IdProductDescription = @currentIdProductDescription;

--8. ��������� �������� ��������
declare @currentIdProduct varchar(50)='1', 
		@newDescription varchar(50) ='che';
Update ProductList
	Set Description = @newDescription
	Where IdProduct = @currentIdProduct;

--9. ��������� ������� ����� �� ����������
declare @currentId int='2', 
		@newStatus bit ='false';
Update Menu
	Set Status = @newStatus
	Where IdDish = @currentId;

--10. ��������� �����
declare @currentId int='2', 
		@newPrice money='800', @newDescription varchar(100)='Ooooochen vkusnoe', @newName varchar(50) = 'Och Vkusno';
Update Menu
	Set Name = @newName, Description = @newDescription, 
		Price = @newPrice
	Where IdDish = @currentId;

--11. ����� ���� ����
Select name from menu;

--12. ����� ���� �������
Select * from WorkOrder

--13. ����� ������
Declare @IdOrder int = 1;
Select * from WorkOrder where IdOrder = @IdOrder;

--14. ����� ���������
Select Name from ProductList;

--15. ����� ������� �� ���������� �������
Declare @MinDate date = '2003-02-02', @MaxDate date = '2003-05-05'

Select Sum(WorkOrder.TotalPrice) from WorkOrder 
where WorkOrder.Date < @MaxDate and WorkOrder.Date > @MinDate

--16. ����� ���� ����������
(Select Waiters.Name from Waiters)
Union
(Select Cooks.Name from Cooks)

--17. �������� �����
Declare @IdDish int = 1; 
Update OrderDescription Set OrderDescription.IdDish = 100 where OrderDescription.IdDish = @IdDish
delete from Menu where IdDish = @IdDish


--18. ���������� ��������� ��� ����
declare @nameOfProduct as varchar(20)='Test';
declare @Description as varchar(50)='1';
declare @IdProduct as int='5';
INSERT INTO ProductList (IdProduct, Name, Description)
	VALUES (@IdProduct, @nameOfProduct, @Description);

--19. ���������� ����� � �����
declare @IdOrderDescription as int='4';
declare @OrderId as varchar(50)='1';
declare @AmountOfDish as int='2';
declare @Status as bit='false';
declare @IdDish as int='3';
declare @IdCook as int='2';
INSERT INTO OrderDescription (IdOrderDescription, OrderId, AmountOfDish, Status, IdDish, IdCook)
	VALUES (@IdOrderDescription, @OrderId, @AmountOfDish, @Status, @IdDish, @IdCook);

--������� �������

--1. ����� �������, ��������������� ������� ������
--(��������� ���������� � ������ ������ �� ������ ������)
--��������������� �������: Waiters, Cooks, WorkOrder,
--ProductDecription, OrderDescription, Menu, ProductList
declare @IdDish as int = '1'
Select distinct IdOrder from WorkOrder, Waiters, ProductDescription, OrderDescription, Menu, ProductList, Cooks
where WorkOrder.IdWaiter = Waiters.IdWaiter and WorkOrder.IdOrder
= ProductDescription.OrderId and ProductDescription.IdProduct
= ProductList.IdProduct and WorkOrder.IdOrder = OrderDescription.OrderId 
and OrderDescription.IdDish = Menu.IdDish and Menu.IdDIsh = @IdDish

--2. ����� ���� ������ ��������� ���������� �������
--(��������� ���������� �� ���������� ������ �� ����������
--���������)
--��������������� �������: Order, Waiters
declare @Name as Varchar(50) = 'Ammm'
Select IdOrder from WorkOrder, Waiters where WorkOrder.IdWaiter = Waiters.IdWaiter and Waiters.Name = @Name

--3. ����� ���������� ������
--(��������� ���������� �� ���������� ������� �� ����������
--������)
--��������������� �������: Waiters, Cooks, Order,
--ProductDecription, OrderDescription, Menu, ProductList
declare @IdOrder as int = '1'
Select  Distinct WorkOrder.*, Menu.Name as Dishes, Menu.Price as Price, OrderDescription.AmountOfDish as Amount from WorkOrder, Waiters, ProductDescription, OrderDescription, Menu, ProductList, Cooks
where WorkOrder.IdWaiter = Waiters.IdWaiter and WorkOrder.IdOrder
= ProductDescription.OrderId and ProductDescription.IdProduct
= ProductList.IdProduct and WorkOrder.IdOrder = OrderDescription.OrderId 
and OrderDescription.IdDish = Menu.IdDish and WorkOrder.IdOrder = @IdOrder

--4. ����� ���� ������� ����, ��������������� ������� ������
--(��������� ���������� � ������ ������ �� ������ ������)
--��������������� �������: Menu, OrderDescription, Order, Cooks
declare @IdCook as int = '1'
Select Menu.Name from Menu, OrderDescription, WorkOrder, Cooks
where Menu.IdDish = OrderDescription.IdDish and WorkOrder.IdOrder = OrderDescription.OrderId and Cooks.IdCook = OrderDescription.IdCook and Cooks.IdCook = @IdCook;

--5. ����� ���������, ������� ������������� � �������
--(��������� ���������� � ������ ������ �� ������ ������)
--��������������� �������: ProductList, ProductDescription, Order
Select Distinct ProductList.Name from ProductList
join ProductDescription on ProductDescription.IdProduct = ProductList.IdProduct
join WorkOrder on WorkOrder.IdOrder = ProductDescription.OrderId

--6. ����� ����������, ������� �������� ��� ��������
--(��������� ���������� � ������ ������ �� ������ ������)
--��������������� �������:�Users, Cooks, Waiters, WorkOrder,
--OrderDescription
Select Distinct Waiters.Name from Waiters
join WorkOrder on WorkOrder.IdWaiter = Waiters.IdWaiter
Union
(Select Distinct Cooks.Name from Cooks
Join OrderDescription on OrderDescription.IdCook = Cooks.IdCook)


--�������������:

--1. ����� ���� ��������� �� �������� �� ������������ ?
GO
Alter View POPULAR_PRODUCTS(Name, Amount) as
select top 10 Name, SUM(ProductDescription.AmountOfProductInGm) from productList, 
ProductDescription where ProductDescription.IdProduct = ProductList.IdProduct
Group by Name
Order by SUM(ProductDescription.AmountOfProductInGm) desc
GO

Select * FROM POPULAR_PRODUCTS;

--2. ����� �������� ����� ���������� ����
GO
Alter View POPULAR_DISHES(Name, Popularnost) as
select top 2  Name, SUM(OrderDescription.AmountOfDish)
  from OrderDescription, 
Menu where Menu.IdDish = OrderDescription.IdDish
Group by Name
Order by SUM(OrderDescription.AmountOfDish) desc
GO

Select * FROM POPULAR_DISHES;

--���������:

--1. ���������� ������� � ����
GO
CREATE PROCEDURE ADD_DISH_IN_MENU(@IdDish as int, @Name as varchar(50), @Description as varchar(100), @Price as money, 
									@Status as bit)  AS
	INSERT INTO Menu (IdDish, Name, Description, Price, Status)
	VALUES (@IdDish, @Name, @Description, @Price, @Status) 
GO

declare @IdDish int='7', @Name varchar(50)='Procedure', @Description varchar(100)='Proverka', @Price money='100', 
									@Status bit = 'true';

EXEC ADD_DISH_IN_MENU @IdDish, @Name, @Description, @Price, @Status


--2. ���������� �������������
GO
CREATE PROCEDURE REGISTER_COOKS(@IdUser as int, @login as varchar(50), @password as varchar(50), @IdCook as int, @name as varchar(50), @dateOfBirth as date, 
									 @phoneNumber as varchar(15), @mail as varchar(50), @status as bit)  AS
	INSERT INTO Users (IdUser, login, password) VALUES (@IdUser, @login, @password)
	INSERT INTO Cooks(IdCook, IdUser, Name, DateOfBirth, PhoneNumber, Mail, Status) 
		VALUES (@IdCook, @IdUser, @name, @dateOfBirth, @phoneNumber, @mail, @Status)
GO

declare @IdUser int = 12, @login varchar(50)='aaa', @password varchar(50)='aaa', @name varchar(50)='testCook', @dateOfBirth date='04-04-2000', @phoneNumber varchar(15)='88888888888', @mail varchar(50)='aaa@gmail.com', @Status bit = 'true', @IdCook int = 12;

EXEC REGISTER_COOKS @IdUser, @login, @password, @IdCook, @name, @dateOfBirth, @phoneNumber, @mail, @Status

GO
CREATE PROCEDURE REGISTER_WAITER(@IdUser as int, @login as varchar(50), @password as varchar(50), @IdWaiter as int, @name as varchar(50), @dateOfBirth as date, 
									 @phoneNumber as varchar(15), @mail as varchar(50), @status as bit)  AS
	INSERT INTO Users (IdUser, login, password) VALUES (@IdUser, @login, @password)
	INSERT INTO Waiters(IdWaiter, IdUser, Name, DateOfBirth, PhoneNumber, Mail, Status) 
		VALUES (@IdWaiter, @IdUser, @name, @dateOfBirth, @phoneNumber, @mail, @Status)
GO

declare @IdUser int = 13, @login varchar(50)='bbb', @password varchar(50)='bbb', @name varchar(50)='testWaiter', @dateOfBirth date='04-04-2000', @phoneNumber varchar(15)='99999999999', @mail varchar(50)='bbb@gmail.com', @Status bit = 'true', @IdWaiter int = 13;

EXEC REGISTER_WAITER @IdUser, @login, @password, @IdWaiter, @name, @dateOfBirth, @phoneNumber, @mail, @Status


--3. ���������� ����� ��������� � �����
GO
CREATE PROCEDURE TOTAL_SUM(@IdOrder as int)  AS
	UPDATE WorkOrder SET TotalPrice = ((Select SUM(Menu.Price*AmountOfDish)
	from Menu join OrderDescription on OrderDescription.IdDish = Menu.IdDish join WorkOrder
	on WorkOrder.IdOrder = OrderDescription.OrderId where WorkOrder.IdOrder = @IdOrder)) where WorkoRder.IdOrder = @IdOrder
GO

declare @IdOrder int ='1'

EXEC TOTAL_SUM @IdOrder 