# Write your MySQL query statement below
Select S.score ,Count(S2.SCORE) as 'rank' From SCORES S,
(Select Distinct SCORE From SCORES) S2
Where S.SCORE<=S2.SCORE
Group By S.ID
ORDER BY S.SCORE DESC