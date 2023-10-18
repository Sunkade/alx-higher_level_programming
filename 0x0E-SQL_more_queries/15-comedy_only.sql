-- Select the title from the tv_shows table
-- Perform two joins: first between tv_shows and tv_show_genres, then between tv_genres and tv_show_genres
-- Filter the results to include only rows where the genre name is 'Comedy'
-- Order the results by title
SELECT title
FROM tv_shows
JOIN tv_show_genres ON id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
