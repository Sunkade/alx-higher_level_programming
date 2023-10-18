-- Select the title from the tv_shows table
-- Exclude TV shows associated with the genre "Comedy"
-- Order the results by TV show title
SELECT title
FROM tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id
      FROM tv_shows
      JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
      JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
      WHERE tv_genres.name = "Comedy"
)
ORDER BY tv_shows.title;
