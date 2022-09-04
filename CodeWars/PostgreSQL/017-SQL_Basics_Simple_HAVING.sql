SELECT age,
       count(*) AS total_people
FROM people
GROUP BY age
HAVING count(*) >= 10;
