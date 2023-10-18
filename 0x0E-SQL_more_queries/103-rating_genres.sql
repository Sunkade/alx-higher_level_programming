-- Select the name from the tv_genres table and the sum of ratings
-- Perform two JOIN operations to link the three tables: hbtn_0d_tvshows_rate, tv_show_genres, and tv_genres
-- Group the results by genre_id to get the sum of ratings for each genre
-- Order the results in descending order by the sum of ratings
SELECT tv_genres.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM hbtn_0d_tvshows_rate
JOIN tv_show_genres ON hbtn_0d_tvshows_rate.show_id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.id
ORDER BY rating_sum DESC;
