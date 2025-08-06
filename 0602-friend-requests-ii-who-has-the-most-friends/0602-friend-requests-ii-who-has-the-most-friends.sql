# Write your MySQL query statement below
With all_ids As (
    Select requester_id As id
    From RequestAccepted
    Union All
    Select accepter_id As id
    From RequestAccepted
) Select id, num
From (
    Select id, Count(id) As num, Rank () Over(Order By Count(id) Desc) As rnk
    From all_ids
    Group By id
)t0
Where rnk = 1