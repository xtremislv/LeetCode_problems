# Write your MySQL query statement below
Select name as Customers
From Customers
Where id not in (
    select customerId
    From Orders
)