# Write your MySQL query statement below
Select visited_on, (
    Select Sum(amount)
    From customer
    Where visited_on Between Date_sub(c.visited_on, Interval 6 Day) And c.visited_on
) As amount,
Round(
    (
        Select Sum(amount) / 7
        From customer
        Where visited_on Between Date_Sub(c.visited_on, Interval 6 Day) And c.visited_on
    ), 2
) As average_amount
From customer c
Where visited_on >= (
    Select Date_Add(Min(visited_on), Interval 6 Day)
    From customer
)
Group By visited_on