SELECT
    *
FROM
    product
WHERE
    to_tsvector(name) @@ to_tsquery('Awesome');