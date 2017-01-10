-- https://community.modeanalytics.com/sql/tutorial/sql-between/

/* Write a query that shows all top 100 songs from January 1, 1985 through December 31, 1990. */

SELECT *
FROM   tutorial.billboard_top_100_year_end
WHERE  year BETWEEN 1985 AND 1990;


-- Notes

-- BETWEEN includes the range bounds (in this case, 1985 and 1990) that you specify in the query, in addition to the values between them. So the above query will return the exact same results as the following query:

SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE year >= 1985 AND <= 1990;