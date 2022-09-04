SELECT min(score),
       percentile_cont(0.5) WITHIN GROUP (ORDER BY score) AS median, -- 50 percentile is a median
       max(score)
FROM result;