-- https://community.modeanalytics.com/sql/tutorial/sql-select-statement/

/* Write a query to select all of the columns in the tutorial.us_housing_units table without using *.
*/

SELECT year,
       month,
       month_name,
       south,
       west,
       midwest,
       northeast
FROM   tutorial.us_housing_units;

/* Write a query to select all of the columns in tutorial.us_housing_units and rename them so that their first letters are capitalized. */

SELECT year AS "Year",
       month AS "Month",
       month_name AS "Month_name",
       south AS "South",
       west AS "West",
       midwest AS "Midwest",
       northeast AS "Northeast"
FROM   tutorial.us_housing_units;