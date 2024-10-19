# 181-mployees-earning-more-than-their-managers

# Write your MySQL query statement below
Select E.name as Employee from Employee E
left join Employee M
on E.managerId = M.id
where E.salary > M.salary;