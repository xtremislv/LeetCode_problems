# Write your MySQL query statement below
Select user_id, Count(user_id) As followers_count
From followers
Group By user_id
Order By user_id Asc