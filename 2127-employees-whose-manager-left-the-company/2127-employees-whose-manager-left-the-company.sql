# Write your MySQL query statement below
Select employee_id
From Employees
Where salary < 30000 And manager_id Not In (
    Select employee_id From Employees
)
Order By employee_id