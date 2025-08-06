# Write your MySQL query statement below
With first_logins As (
    Select A.player_id, Min(A.event_date) As first_login
    From Activity A
    Group By A.player_id
), consec_logins As (
    Select Count(A.player_id) As num_logins
    From first_logins F Inner Join Activity A On F.player_id = A.player_id And F.first_login = DATE_SUB(A.event_date, Interval 1 Day)
)
Select Round(
    (Select C.num_logins From consec_logins C)
    / (Select Count(F.player_id) From first_logins F), 2) As fraction