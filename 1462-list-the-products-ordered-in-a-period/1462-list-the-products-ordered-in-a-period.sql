# Write your MySQL query statement below
Select p.product_name As product_name, Sum(o.unit) As unit From Products p
Join Orders o Using (product_id)
Where Year(o.order_date)='2020' And Month(o.order_date)='02'
Group By p.product_id
Having Sum(o.unit)>=100