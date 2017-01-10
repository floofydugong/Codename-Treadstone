-- https://community.modeanalytics.com/sql/tutorial/sql-like/

/* Write a query that returns all rows for which Ludacris was a member of the group. */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE "group" ILIKE '%Ludacris%';


/* Write a query that returns all rows for which the first artist listed in the group has a name that begins with "DJ". */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE "group" ILIKE 'DJ%';

-- Notes
-- You can also use a underscore to fill in spaces

SELECT *
  FROM tutorial.billboard_top_100_year_end
 WHERE artist ILIKE 'dr_ke';
