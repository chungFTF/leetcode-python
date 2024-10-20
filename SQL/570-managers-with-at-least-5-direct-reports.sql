# 570-managers-with-at-least-5-direct-reports


# Sol 1
-- SELECT Mgr.name
-- FROM Employee Emp
-- JOIN Employee Mgr
-- ON Mgr.id = Emp.managerId
-- GROUP BY Mgr.id
-- HAVING COUNT(Mgr.id) >= 5;

# Sol 2

SELECT name 
FROM Employee 
WHERE id IN (
    SELECT managerId 
    FROM Employee 
    GROUP BY managerId 
    HAVING COUNT(*) >= 5)