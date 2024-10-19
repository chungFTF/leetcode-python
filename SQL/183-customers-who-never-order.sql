# 183-customers-who-never-order

# Sol 1
-- Select name as Customers from Customers C
-- left join Orders O
-- on O.customerId = C.id
-- where O.customerId is NULL;


# Sol 2
Select name as Customers 
From Customers
Where id not in (
    Select customerId from Orders
);