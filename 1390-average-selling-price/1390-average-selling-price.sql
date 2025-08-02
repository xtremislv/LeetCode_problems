# Write your MySQL query statement below
Select p.product_id, Ifnull(Round(Sum(p.price*u.units) / Sum(u.units), 2), 0) As average_price
From Prices As p Left Join UnitsSold As u 
On p.product_id = u.product_id And u.purchase_date Between p.start_date And p.end_date
Group By p.product_id