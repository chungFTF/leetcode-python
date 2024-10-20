# 197-rising-temperature

# Sol 1
-- SELECT W1.id
-- FROM Weather W1
-- JOIN Weather W2
-- ON W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY)
-- WHERE W1.temperature > W2.temperature;


# Sol 2
SELECT today.id
FROM Weather today
CROSS JOIN Weather yesterday
WHERE DATEDIFF(today.recordDate,yesterday.recordDate) = 1
AND today.temperature > yesterday.temperature;
