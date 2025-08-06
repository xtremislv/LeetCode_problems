# Write your MySQL query statement below
Select customer_id From Customer Group By customer_id
Having Count(distinct product_key) = (Select Count(product_key) From Product)