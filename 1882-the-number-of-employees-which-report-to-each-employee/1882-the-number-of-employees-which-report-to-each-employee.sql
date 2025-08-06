# Write your MySQL query statement below
Select reports_to As employee_id,
(
    Select name
    From employees e1
    Where e.reports_to = e1.employee_id
) As name,
Count(reports_to) As reports_count,
Round(Avg(age)) As average_age
From employees e
Group By reports_to
Having reports_count > 0
Order By employee_id