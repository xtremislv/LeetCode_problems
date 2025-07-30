Select customer_id, count(*) As count_no_trans
From Visits As v Left Join Transactions As T On v.visit_id = T.visit_id
Where transaction_id is Null
Group By customer_id