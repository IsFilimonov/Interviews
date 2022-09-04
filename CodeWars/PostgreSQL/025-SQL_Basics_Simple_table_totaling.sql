SELECT DISTINCT clan,
  rank() OVER (ORDER BY sum(points) DESC) AS rank,
  coalesce(nullif(clan,''), '[no clan specified]') AS clan,
  sum(points) AS total_points,
  count(name) AS total_people
FROM people
GROUP BY clan
ORDER BY total_points DESC,rank ASC;