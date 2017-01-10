-- https://community.modeanalytics.com/sql/tutorial/sql-or-operator/

/* Write a query that returns all rows for top-10 songs that featured either Katy Perry or Bon Jovi. */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE year_rank <= 10
AND  ("group" ILIKE '%Bon Jovi%' OR "group" ILIKE '%Katy Perry%');

/* Write a query that returns all songs with titles that contain the word "California" in either the 1970s or 1990s. */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE song_name ILIKE '%California%'
AND (year >= 1970 AND year < 1980 OR year >= 1990 AND year < 2000);

/* Write a query that lists all top-100 recordings feature Dr. Dre before 2001 or after 2009. */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE (year < 2001 OR year > 2009)
AND "group" ILIKE '%Dr. Dre%';

-- Notes
-- The last one is a bit tricky, having to put parentheses around the OR condition