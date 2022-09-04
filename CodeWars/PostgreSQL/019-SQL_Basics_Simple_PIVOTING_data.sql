CREATE EXTENSION tablefunc;
-- BEST Practices
SELECT * 
FROM  crosstab(
      'SELECT p.name, detail, COUNT(d.id)
      FROM products p
      JOIN details d
      ON p.id = d.product_id
      GROUP BY p.name, d.detail
      ORDER BY 1,2')
AS ct (name text, bad bigint, good bigint, ok bigint)

--My solution. I don't understand why not it accepted.
/*
SELECT *
FROM crosstab(
'SELECT p.name   AS name,
        d.detail AS detail,
        count(d.id) AS count
FROM products p
	JOIN details d
		ON p.id = d.product_id
GROUP BY p.name, d.detail
ORDER BY p.name, d.detail')
AS final_result(name text, good bigint, ok bigint, bad bigint);
*/