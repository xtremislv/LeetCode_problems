# Write your MySQL query statement below
Select query_name, Round(Avg(Cast(rating As decimal) / position), 2) As quality, Round(Sum(Case When rating < 3 Then 1 Else 0 End) * 100 / Count(*), 2) As poor_query_percentage
From Queries Group By query_name