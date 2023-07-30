-- Script list all shows without the genre Comedy
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- Use a maximum of two SELECT statement
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT show_id FROM tv_show_genres
    WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
)
ORDER BY title ASC;
