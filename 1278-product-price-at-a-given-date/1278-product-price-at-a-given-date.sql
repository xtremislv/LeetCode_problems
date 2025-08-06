# Write your MySQL query statement below
Select product_id, IFNULL (price, 10) AS price
From (
    Select Distinct product_id
    From Products
) As UniqueProducts
Left Join (
    Select Distinct product_id, FIRST_VALUE (new_price) Over (
        Partition By product_id
        Order By change_date Desc
    ) As price
    From Products
    Where change_date <= '2019-08-16'
) As LastChangedPrice Using (product_id)