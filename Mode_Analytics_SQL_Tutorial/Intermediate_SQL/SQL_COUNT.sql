-- https://community.modeanalytics.com/sql/tutorial/sql-count/

/* Write a query to count the number of non-null rows in the low column. */
SELECT COUNT(low)
FROM tutorial.aapl_historical_stock_price;

/* Write a query that determines counts of every single column. Which column has the most null values? */

SELECT COUNT(year) as year_count,
       COUNT(month) as month_count,
       COUNT(open) as open_count,
       COUNT(high) as high_count,
       COUNT(low) as low_count,
       COUNT(close) as close_count,
       COUNT(volume) volume_count
FROM tutorial.aapl_historical_stock_price;

-- High Count has the most null values