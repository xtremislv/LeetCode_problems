# Write your MySQL query statement below
Select S.user_id , Round(if ((confirmed / total) is Null , 0 , (confirmed / total)), 2) As confirmation_rate
From Signups S Left Join (
    Select user_id , Count(action) As total
    From Confirmations
    Group By user_id
) T On S.user_id = T.user_id Left Join(
    Select user_id , Count(action) As confirmed
    From Confirmations
    Where action = 'confirmed'
    Group By user_id
) C On T.user_id = C.user_id



