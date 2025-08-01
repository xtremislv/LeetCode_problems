# Write your MySQL query statement below
Select E1.name
From Employee E1
Join(
    Select managerId, count(*) As directReports
    From Employee
    Group By managerId
    Having Count(*) >= 5
) E2 On e1.id = e2.managerId
