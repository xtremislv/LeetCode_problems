# Write your MySQL query statement below
Select u.product_name, Sales.year, Sales.price
From Sales left Join Product As u ON Sales.product_id = u.product_id Order By year