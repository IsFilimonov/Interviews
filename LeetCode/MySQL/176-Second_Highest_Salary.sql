SELECT
    (SELECT DISTINCT Salary
     FROM Employee
     ORDER BY Salary DESC
     LIMIT 1
     OFFSET 1) AS SecondHighestSalary ;

/* PG window
WITH cte AS
    (SELECT salary,
            row_number() OVER (
                               ORDER BY salary)
     FROM employee)
SELECT salary AS SecondHighestSalary
FROM cte
WHERE row_number = 2;
*/ ;

/* PG distinct + limit + offset
WITH cte AS
    (SELECT DISTINCT salary
     FROM employee
     ORDER BY salary)
SELECT salary AS SecondHighestSalary
FROM cte
LIMIT 1
OFFSET 1;
*/ ;