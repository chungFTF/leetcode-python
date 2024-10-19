# 175-combine-two-tables

# Write your MySQL query statement below

# Sol 1
-- Select Person.firstName, Person.lastName, Address.city, Address.state from Person 
-- Left join Address 
-- on Person.personId = Address.personId;


# Sol 2
SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A USING (personId);