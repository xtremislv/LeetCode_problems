# Write your MySQL query statement below
Select u.unique_id, Employees.name
From Employees
Left Join EmployeeUNI AS u
On Employees.id = u.id