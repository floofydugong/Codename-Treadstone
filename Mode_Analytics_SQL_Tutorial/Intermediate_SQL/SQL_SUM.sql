-- https://community.modeanalytics.com/sql/tutorial/sql-sum/

/* Write a query to calculate the average opening price (hint: you will need to use both COUNT and SUM, as well as some simple arithmetic.). */

SELECT SUM(open)/COUNT(open)
FROM tutorial.aapl_historical_stock_price;

-- Notes
-- You have to use "open" instead of * for the COUNT beacuse using COUNT will count NULLS if you do