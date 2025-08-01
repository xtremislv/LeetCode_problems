# Write your MySQL query statement below
Select *
From Cinema
Where description != 'boring' And Mod(id, 2) != 0
Order by rating Desc