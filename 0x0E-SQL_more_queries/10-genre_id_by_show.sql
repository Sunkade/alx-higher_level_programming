-- Select the title from the tv_shows table and genre_id from the tv_show_genres table
-- Join the tv_shows and tv_show_genres tables on the condition that tv_shows.id matches tv_show_genres.show_id
-- Results are ordered by title and then by genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
