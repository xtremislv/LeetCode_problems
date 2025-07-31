# Write your MySQL query statement below
Select w2.id
From Weather w1, Weather w2
Where Datediff(w2.recordDate, w1.recordDate) = 1 And w2.temperature > w1.temperature