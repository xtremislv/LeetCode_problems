# Write your MySQL query statement below
Select Left(trans_date, 7) As month, country, Count(id) As trans_count, Sum(state = 'approved') As approved_count, Sum(amount) As trans_total_amount, Sum((state = 'approved') * amount) As approved_total_amount
From Transactions Group By month, country