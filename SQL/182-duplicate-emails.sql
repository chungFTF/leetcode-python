# 182-duplicate-emails

# Write your MySQL query statement below
select email as Email from Person P
group by email 
having count(email) > 1;