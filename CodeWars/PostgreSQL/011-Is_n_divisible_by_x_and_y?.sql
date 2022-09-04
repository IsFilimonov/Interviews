SELECT id,
       CASE
           WHEN mod(n, x) = 0 AND mod(n, y) = 0 THEN TRUE
           ELSE FALSE
           END AS res
FROM kata;

--BEST PRACTICE
--SELECT id, n % x = 0 AND n % y = 0 AS res
--FROM kata;