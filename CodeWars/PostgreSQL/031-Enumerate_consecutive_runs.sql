--My
/*
Note: also need to check spaces between ids
Strategy: there are two ways to break consecutive:
	- miss id: 1, 2, 3, 5, 6
	- change next value: 1, 1, 1, 2, 2
OPERATOR OR:
true OR true: true
true OR false: true
true OR null: true
false or false: false
false or null: null
null or null: null
*/ 
SELECT id,
       value,
       sum(CASE WHEN change THEN 1 ELSE 0 END) OVER (ORDER BY id) as run_id
FROM (
         SELECT id,
                value,
-- if next value changed: then (TRUE) consecutive break
                (value <> LAG(value, 1, 1) OVER (ORDER BY id))
-- if next id missed: then (TRUE) consecutive break
             OR ((id - 1) <> LAG(id) OVER (ORDER BY id)) AS change
         FROM entries) as sub;


--BEST:
SELECT id, 
       value, 
       SUM(run_id) OVER(ORDER BY id) AS run_id
FROM (SELECT id, 
             value, 
             CASE value = (LAG(value) OVER(ORDER BY id)) AND (id-1) = (LAG(id) OVER(ORDER BY id))
                 WHEN TRUE THEN 0
                 ELSE 1
             END AS run_id
       FROM entries
     ) helper
ORDER BY id