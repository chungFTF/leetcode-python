# 1581-product-sales-analysis-i

# Sol 1
-- SELECT customer_id, COUNT(customer_id) AS count_no_trans
-- FROM Visits V
-- LEFT JOIN Transactions T
-- ON V.visit_id = T.visit_id
-- WHERE transaction_id is NULL
-- GROUP BY customer_id;

# Sol 2

SELECT customer_id, COUNT(visit_id) AS count_no_trans
FROM Visits 
WHERE visit_id NOT IN (
    SELECT visit_id
    FROM Transactions
)
GROUP BY customer_id;