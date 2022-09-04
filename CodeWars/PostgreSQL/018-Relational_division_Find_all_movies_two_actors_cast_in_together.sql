WITH id105 AS (SELECT film_id
               FROM film_actor
               WHERE actor_id = 105),
     id122 AS (SELECT film_id
               FROM film_actor
               WHERE actor_id = 122),
     t     AS (SELECT t105.film_id
               FROM id105 t105
                         INNER JOIN id122 t122
                         ON t105.film_id = t122.film_id)
SELECT f.title AS title
FROM t
          LEFT JOIN film f
          ON t.film_id = f.film_id;

/*BEST PRACTICES*/
/*
SELECT f.title
FROM film f
JOIN film_actor fa on fa.film_id = f.film_id
WHERE fa.actor_id IN (105,122)
GROUP BY f.film_id
HAVING COUNT(*) = 2
ORDER BY f.title ASC
*/