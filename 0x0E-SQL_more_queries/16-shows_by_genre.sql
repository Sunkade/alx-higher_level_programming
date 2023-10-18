-- Select the title from the tv_shows table and name from the tv_genres table
-- Perform two LEFT JOINs: first between tv_shows and tv_show_genres, then between tv_show_genres and tv_genres
-- Ensure that all records from tv_shows are included, even if there are no matches in tv_show_genres and tv_genres
-- Results are ordered by title and then by genre name
SELECT title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;
