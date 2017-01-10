-- https://community.modeanalytics.com/sql/tutorial/sql-and-operator/

/* Write a query that surfaces all rows for top-10 hits for which Ludacris is part of the Group. */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE year_rank <= 10
AND "group" ILIKE '%Ludacris%';

/* Write a query that surfaces the top-ranked records in 1990, 2000, and 2010 */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE year in (1990,2000,2010)
AND year_rank = 1;

/* Write a query that lists all songs from the 1960s with "love" in the title. */

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE year >= 1960
AND year < 1970
AND song_name ILIKE '%love%';