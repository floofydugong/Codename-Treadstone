-- https://community.modeanalytics.com/sql/tutorial/sql-operators/

/* Did the West Region ever produce more than 50,000 housing units in one month? */

SELECT *
FROM tutorial.us_housing_units
WHERE west > 50;

/* Did the South Region ever produce 20,000 or fewer housing units in one month? */

SELECT *
FROM tutorial.us_housing_units
WHERE south <= 20;

/* Write a query that only shows rows for which the month name is February. */

SELECT *
FROM tutorial.us_housing_units
WHERE month_name = 'February';

/* Write a query that only shows rows for which the month_name starts with the letter "N" or an earlier letter in the alphabet. */

SELECT *
FROM tutorial.us_housing_units
WHERE month_name <= 'N';

/* Write a query that calculates the sum of all four regions in a separate column. */

SELECT * , west + south + midwest + northeast AS usa_total
FROM tutorial.us_housing_units;

/* Write a query that returns all rows for which more units were produced in the West region than in the Midwest and Northeast combined. */

SELECT *
FROM tutorial.us_housing_units
WHERE west > (midwest+northeast);

/* Write a query that calculates the percentage of all houses completed in the United States represented by each region. Only return results from the year 2000 and later. */

SELECT south/(south+west+midwest+northeast) * 100 AS south_percentage,
       west/(south+west+midwest+northeast) * 100 AS west_percentage,
       midwest/(south+west+midwest+northeast) * 100 AS midwest_percentage,
       northeast/(south+west+midwest+northeast) * 100 AS northeast_percentage
FROM tutorial.us_housing_units
WHERE year >= 2000