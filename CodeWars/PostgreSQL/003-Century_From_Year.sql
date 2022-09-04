SELECT CASE
           WHEN yr % 100 = 0 THEN yr / 100
           WHEN yr % 100 > 0 THEN (yr / 100) + 1
           END century
FROM years;

--BEST PRACTICE
--Nearest int >= argument
--But I don't understand why it accepted
-- SELECT CEILING(yr / 100.00) AS century
-- FROM years