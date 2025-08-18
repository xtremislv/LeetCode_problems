# Write your MySQL query statement below
Select email From Person
Group By email
Having COUNT(email) > 1