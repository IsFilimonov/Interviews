SELECT
    id,
    CASE WHEN base % factor = 0 THEN
        TRUE
    ELSE
        FALSE
    END AS res
FROM
    kata;