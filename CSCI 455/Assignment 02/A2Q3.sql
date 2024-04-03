SELECT e.Fname, e.Lname
FROM EMPLOYEE e
WHERE e.Super_ssn = (SELECT Ssn FROM EMPLOYEE WHERE Fname = 'Franklin');