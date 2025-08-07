# Write your MySQL query statement below
Select (
    Select Distinct salary
    From Employee
    Order By salary Desc
    Limit 1 OFFSET 1
) AS SecondHighestSalary