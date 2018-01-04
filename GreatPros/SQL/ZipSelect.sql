.read DecLeadsparsed.sql

SELECT Zip, Count(*) FROM DecLeadsparsed GROUP BY Zip HAVING Count(*) > 10 ORDER BY Count(*) DESC;
