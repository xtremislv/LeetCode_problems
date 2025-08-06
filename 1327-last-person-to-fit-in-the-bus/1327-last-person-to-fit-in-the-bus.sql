# Write your MySQL query statement below
Select q1.person_name
From Queue q1 Join Queue q2 On q1.turn >= q2.turn
Group By q1.turn
Having Sum(q2.weight) <= 1000
Order By Sum(q2.weight) Desc
Limit 1