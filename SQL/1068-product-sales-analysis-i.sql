# 1068-product-sales-analysis-i

SELECT P.product_name, year, price
FROM Sales S
INNER JOIN Product P
ON S.product_id = P.product_id;