# Write your MySQL query statement below
Select e.name , u.bonus
From Employee e Left Join Bonus As u On e.empId = u.empId
Where u.bonus < 1000 Or u.bonus is Null