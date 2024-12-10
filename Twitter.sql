WITH derived as(
  SELECT user_id, COUNT(1) as tweet_bucket
  FROM tweets
  WHERE EXTRACT(YEAR FROM tweet_date) = '2022'
  GROUP BY user_id
)

SELECT 
  tweet_bucket, COUNT(1) as users_num
FROM derived
GROUP BY tweet_bucket
ORDER BY tweet_bucket;
