-- Select the name from the tv_genres table, aliasing it as 'genre'
-- Count the number of shows for each genre
-- Perform an inner join between tv_genres and tv_show_genres on genre_id
-- Group the results by tv_show_genres.genre_id
-- Order the results by the number of shows in descending order
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
