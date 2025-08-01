# Write your MySQL query statement below
Select S.student_id, S.student_name, Su.subject_name, Count(E.student_id) attended_exams
From Students S Cross Join Subjects Su Left Join Examinations E
On S.student_id = E.student_id And Su.subject_name = E.subject_name
Group By S.student_id, S.student_name, Su.subject_name
Order By S.student_id, S.student_name, Su.subject_name