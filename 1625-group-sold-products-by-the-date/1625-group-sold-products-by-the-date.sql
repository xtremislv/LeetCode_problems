# Write your MySQL query statement below
Select sell_date, Count(Distinct product) As num_sold, GROUP_CONCAT(Distinct product Order By product ASC separator ',') As products
From Activities Group By sell_date Order By sell_date Asc