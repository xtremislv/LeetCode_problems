# Write your MySQL query statement below
Select contest_id, Round(Count(Distinct user_id) * 100 / (Select Count(user_id) From Users), 2) As percentage
From Register
Group By contest_id
Order By percentage Desc, contest_id