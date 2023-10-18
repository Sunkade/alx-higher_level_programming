-- Select the title from the tv_shows table and genre_id from the tv_show_genres table
-- Perform a LEFT JOIN to include all records from tv_shows, even if there is no match in tv_show_genres
-- Filter the results to include only rows where there is no matching record in tv_show_genres
-- Results are ordered by title and then by genre_id
SELECT title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
