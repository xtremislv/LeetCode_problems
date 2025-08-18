# Write your MySQL query statement below
SELECT e2.name as Employee
From employee e1
Inner Join employee e2 On e1.id = e2.managerID
Where e1.salary < e2.salary