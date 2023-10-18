-- Select the name from the tv_genres table
-- Perform two joins: first between tv_genres and tv_show_genres, then between tv_shows and tv_show_genres
-- Filter the results to include only rows where the title of the TV show is 'Dexter'
-- Order the results by name
SELECT name
FROM tv_genres
JOIN tv_show_genres ON id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
