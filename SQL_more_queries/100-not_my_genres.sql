-- Script list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- Use a maximum of two SELECT statement
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id FROM tv_show_genres
    WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
    )
ORDER BY name ASC;