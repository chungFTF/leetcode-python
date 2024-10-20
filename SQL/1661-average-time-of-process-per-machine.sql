# 1661-average-time-of-process-per-machine

# Sol 2
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp),3) as processing_time
FROM Activity a1
JOIN Activity a2
ON a1.process_id = a2.process_id AND a1.machine_id = a2.machine_id
AND a1.timestamp < a2.timestamp
GROUP BY a1.machine_id;

# Sol 1
-- SELECT S.machine_id, ROUND(AVG(E.timestamp - S.timestamp), 3) AS processing_time
-- FROM (
--     SELECT * 
--     FROM  Activity
--     WHERE activity_type = "start"
-- ) S
-- JOIN (
--     SELECT * 
--     FROM  Activity
--     WHERE activity_type = "end"
-- ) E
-- ON E.machine_id = S.machine_id and E.process_id = S.process_id
-- GROUP BY S.machine_id;

