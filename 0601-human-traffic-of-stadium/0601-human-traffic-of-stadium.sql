# Write your MySQL query statement below
SELECT 
    DISTINCT a.*
FROM 
    stadium AS a, stadium AS b, stadium AS c
WHERE
     a.people >= 100 AND b.people >= 100 AND c.people >= 100
AND 
    (
       (a.id - b.id = 1 AND b.id - c.id = 1)
    OR (c.id - b.id = 1 AND b.id - a.id = 1)
    OR (b.id - a.id = 1 AND a.id - c.id = 1)
    )
ORDER BY visit_date