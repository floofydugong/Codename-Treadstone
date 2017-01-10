-- https://community.modeanalytics.com/sql/tutorial/sql-is-null/

/* Write a query that shows all of the rows for which song_name is null. */

SELECT *
FROM   tutorial.billboard_top_100_year_end
WHERE  song_name IS NULL;


-- Notes

-- WHERE artist = NULL will not work—you can’t perform arithmetic on null values.