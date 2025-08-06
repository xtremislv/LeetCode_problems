# Write your MySQL query statement below
(Select name As results
From MovieRating Join Users Using(user_id)
Group By name
Order By Count(*) Desc, name
Limit 1)
Union All
(Select title As results
From MovieRating Join Movies Using(movie_id)
Where Extract(Year_Month From created_at) = 202002
Group By title
Order By Avg(rating) Desc, title
Limit 1)