-- Select the title from the tv_shows table and genre_id from the tv_show_genres table
-- Perform a LEFT JOIN to include all records from tv_shows, even if there is no match in tv_show_genres
-- Results are ordered by title and then by genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
