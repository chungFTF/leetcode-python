# 1378-replace-employee-id-with-the-unique-identifier

SELECT unique_id, name
FROM Employees E
LEFT JOIN EmployeeUNI EU
ON E.id = EU.id;