# Write your MySQL query statement below
Select project_id, Round(Avg(experience_years), 2) As average_years
From project p Join Employee e On p.employee_id = e.employee_id
Group By project_id