# 184-department-highest-salary

# Write your MySQL query statement below

SELECT D.name AS Department, E.name AS Employee, E.salary
FROM Employee  E
JOIN Department D
ON E.departmentId = D.id
WHERE (departmentId, salary) IN (

   SELECT departmentId,MAX(salary) FROM Employee GROUP BY departmentId

)


