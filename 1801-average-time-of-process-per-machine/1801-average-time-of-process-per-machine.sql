# Write your MySQL query statement below
Select a.machine_id , Round(Avg(b.timestamp - a.timestamp), 3) As processing_time
From Activity a, Activity b
Where a.machine_id = b.machine_id And a.process_id = b.process_id And a.activity_type = 'start' And b.activity_type = 'end'
Group By a.machine_id