-- Task 13: Create a grouping sets query
-- Create a grouping sets query using the columns stationid, trucktype, total waste collected.
SELECT
    t.trucktype,
    s.city,
    s.stationid,
    SUM(f.wastecollected) as "total waste collected"
FROM
    FactTrips f
    INNER JOIN DimStation s ON f.stationid = s.stationid
    INNER JOIN DimTruck t ON f.truckid = t.truckid
GROUP BY
    GROUPING SETS (
        (t.truckType, s.city),
        (t.truckType, s.city, s.stationid)
    )
ORDER BY
    t.trucktype,
    s.city,
    s.stationid;

-- Task 14: Create a rollup query
-- Create a rollup query using the columns year, city, stationid, and total waste collected.
SELECT
    d.year,
    s.city,
    s.stationid,
    SUM(f.wastecollected) as "total waste collected"
FROM
    FactTrips f
    INNER JOIN DimDate d ON f.dateid = d.dateid
    INNER JOIN DimStation s ON f.stationid = s.stationid
GROUP BY
    ROLLUP (d.year, s.city, s.stationid)
ORDER BY
    d.year DESC,
    s.city,
    s.stationid;

-- Task 15: Create a cube query
-- Create a cube query using the columns year, city, stationid, and average waste collected.
SELECT
    d.year,
    s.city,
    s.stationid,
    AVG(f.wastecollected) as "average waste collected"
FROM
    FactTrips f
    INNER JOIN DimDate d ON f.dateid = d.dateid
    INNER JOIN DimStation s ON f.stationid = s.stationid
GROUP BY
    CUBE (d.year, s.city, s.stationid);

-- Task 16: Create a materialized view
-- Create a materialized view named max_waste_stats using the columns city, stationid,
-- trucktype, and max waste collected.
CREATE MATERIALIZED VIEW max_waste_stats AS
SELECT
    t.trucktype,
    s.city,
    s.stationid,
    MAX(f.wastecollected) as "max waste collected"
FROM
    FactTrips f
    INNER JOIN DimStation s ON f.stationid = s.stationid
    INNER JOIN DimTruck t ON f.truckid = t.truckid
GROUP BY
    t.truckType,
    s.city,
    s.stationid
ORDER BY
    t.trucktype,
    s.city,
    s.stationid
WITH
    DATA;

REFRESH MATERIALIZED VIEW max_waste_stats;

SELECT * FROM max_waste_stats;