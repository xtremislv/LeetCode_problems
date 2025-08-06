# Write your MySQL query statement below
Select employee_id, department_id
From (
    Select * , Count(employee_id) Over(Partition By employee_id) As EmployeeCount
    From Employee
) EmployeePartition
Where EmployeeCount = 1
Or primary_flag = 'Y'