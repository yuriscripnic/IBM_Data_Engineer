# Exercise 1: Design a data warehouse

## Task 1: Design the dimension table DimDate
Write down the fields in the DimDate table in any text editor, one field per line. The company is looking at a granularity of day, which means they would like to have the ability to generate the report on a yearly, monthly, daily, and weekday basis.
Take a screenshot of the fieldnames for the table MyDimDate 1-MyDimDate.jpg. 

- dateid
- date
- year
- quarter
- quartername
- month
- monthname
- day
- weekday
- weekdayname

## Task 2: Design the dimension table DimWaste
Write down the fields in the MyDimWaste table in any text editor, one field per line.
Take a screenshot of the fieldnames for the table MyDimWaste 2-MyDimWaste.
WARNING: MyDimWast don't make sense in this task, and it was changed to DimTruck

- truckid
- trucktype

## Task 3: Design the dimension table MyDimZone
Write down the fields in the MyDimZone table in any text editor, one field per line.
Take a screenshot of the fieldnames for the table MyDimZone  3-MyDimZone.jpg.
WARNING: MyDimZone don't make sense in this task, and it was changed to DimStation

- stationid
- city

## Task 4: Design the fact table MyFactTrips
Write down the fields in the MyFactTrips table in any text editor, one field per line.
Take a screenshot of the fieldnames for the table MyFactTrips 4-MyFactTrips.jpg.

- tripid
- dateid
- stationid
- truckid
- wastecollected

# Exercise 2 - Create schema for data warehouse on PostgreSQL
In this exercise, you will create the tables you have designed in the previous exercise. Open pgAdmin and create a database named Project, then create the following tables.

## Task 5: Create the dimension table MyDimDate
Create the MyDimDate table.

DROP TABLE IF EXISTS DimDate;

CREATE TABLE
    DimDate (
        dateid INT PRIMARY KEY,
        date date NOT NULL,
        year INT NOT NULL,
        quarter INT NOT NULL,
        quartername VARCHAR(255) NOT NULL,
        month INT NOT NULL,
        monthname VARCHAR(255) NOT NULL,
        day INT NOT NULL,
        weekday INT NOT NULL,
        weekdayname VARCHAR(255) NOT NULL
    );

Take a screenshot of the SQL statement you used to create the table MyDimDate, name the screenshot 5-MyDimDate.jpg. 

## Task 6: Create the dimension table MyDimWaste
Create the MyDimWaste table.

DROP TABLE IF EXISTS DimTruck;

CREATE TABLE
    DimTruck (
        truckid INT PRIMARY KEY,
        truckType VARCHAR(255) NOT NULL
    );



Take a screenshot of the SQL statement you used to create the table MyDimWaste, name the screenshot 6-MyDimWaste.jpg. 

## Task 7: Create the dimension table MyDimZone
Create the MyDimZone table.
Take a screenshot of the SQL statement you used to create the table MyDimZone, name the screenshot 7-MyDimZone.jpg. 

DROP TABLE IF EXISTS DimStation;

CREATE TABLE
    DimStation (
        stationid INT PRIMARY KEY,
        city VARCHAR(255) NOT NULL
    );


## Task 8: Create the fact table MyFactTrips
Create the MyFactTrips table.
Take a screenshot of the SQL statement you used to create the table MyFactTrips, name the screenshot 8-MyFactTrips.jpg. 

DROP TABLE IF EXISTS FactTrips;

CREATE TABLE
    FactTrips (
        tripid INT PRIMARY KEY,
        wastecollected INT NOT NULL,
        dateid INT REFERENCES DimDate (dateid),
        stationid INT REFERENCES DimStation (stationid),
        truckid INT REFERENCES DimTruck (truckid)
    );




# Exercise 3: Load data into the data warehouse
In this exercise, you will load the data into the tables.

After the initial schema design, you were told that due to operational issues, data could not be collected in the format initially planned. This implies that the previous tables (MyDimDate, MyDimWaste, MyDimZone, MyFactTrips) in the Project database and their associated attributes are no longer applicable to the current design. The company has now provided data in CSV files with new tables DimTruck and DimStation as per the new design.

## Task 9: Load data into the dimension table DimDate
Download the data from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/DimDate.csv
Load this data into DimDate table.
Take a screenshot of the first 5 rows in the table DimDate, name the screenshot 9-DimDate.jpg.
Project=# \copy DimDate from '/home/project/DimDate.csv' delimiter ',' csv header;
COPY 350
Project=# select * from DimDate limit 5;
 dateid |    date    | year | quarter | quartername | month | monthname | day | weekday | weekdayname 
--------+------------+------+---------+-------------+-------+-----------+-----+---------+-------------
      1 | 2019-03-09 | 2019 |       1 | Q1          |     3 | March     |   9 |       7 | Sunday
      2 | 2019-03-10 | 2019 |       1 | Q1          |     3 | March     |  10 |       1 | Monday
      3 | 2019-03-11 | 2019 |       1 | Q1          |     3 | March     |  11 |       2 | Tuesday
      4 | 2019-03-12 | 2019 |       1 | Q1          |     3 | March     |  12 |       3 | Wednesday
      5 | 2019-03-13 | 2019 |       1 | Q1          |     3 | March     |  13 |       4 | Thursday
(5 rows)



## Task 10: Load data into the dimension table DimTruck
Download the data from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/DimTruck.csv
Load this data into DimTruck table.
Take a screenshot of the first 5 rows in the table DimTruck, name the screenshot 10-DimTruck.jpg.

## Task 11: Load data into the dimension table DimStation
Download the data from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/DimStation.csv
Load this data into DimStation table.
Take a screenshot of the first 5 rows in the table DimStation, name the screenshot 11-DimStation.jpg.

## Task 12: Load data into the fact table FactTrips
Download the data from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/FactTrips.csv
Load this data into FactTrips table.
Take a screenshot of the first 5 rows in the table FactTrips, name the screenshot 12-FactTrips.jpg.

# Exercise 4 - Write aggregation queries and create materialized views
In this exercise, you will query the data you have loaded in the previous exercise.

## Task 13: Create a grouping sets query
Create a grouping sets query using the columns stationid, trucktype, total waste collected.
Take a screenshot of the SQL and the output rows, name the screenshot 13-groupingsets.jpg.

## Task 14: Create a rollup query
Create a rollup query using the columns year, city, stationid, and total waste collected.
Take a screenshot of the SQL and the output rows, name the screenshot 14-rollup.jpg.

## Task 15: Create a cube query
Create a cube query using the columns year, city, stationid, and average waste collected.
Take a screenshot of the SQL and the output rows, name the screenshot 15-cube.jpg.

## Task 16: Create a materialized view
Create a materialized view named max_waste_stats using the columns city, stationid, trucktype, and max waste collected.
Take a screenshot of the SQL ,name the screenshot 16-mv.jpg.