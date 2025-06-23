# Data Warehouse Reporting
## Scenario
You are a data engineer hired by an ecommerce company named SoftCart.com . 
The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. 

You have designed the schema for the data warehouse in the previous assignment. Data engineering is a team game. Your senior data engineer reviewed your design. Your schema design was improvised to suit the production needs of the company. In this assignment you will generate reports out of the data in the data warehouse.

## Objectives
In this assignment you will:
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs

## About the dataset
The dataset you would be using in this assignment is not a real life dataset. It was programmatically created for this assignment purpose.

### Prepare the lab environment
Before you start the assignment:

Right Click on this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nm75oOK5n7AGME1F7_OIQg/CREATE-SCRIPT.sql) and save this SQL file in you local system.

### Start PostgreSQL server
Create a new database Test1
Create the following tables
- DimDate
- DimCategory
- DimCountry
- FactSales

```sql
-- Create the table

---------------------------------------
CREATE TABLE public."DimDate"
(
    dateid integer NOT NULL,
    date date,
    Year integer,
    Quarter integer,
    QuarterName character(50),
    Month integer,
    Monthname character(50),
    Day integer,
    Weekday integer,
    WeekdayName character(50),
    CONSTRAINT "DimDate_pkey" PRIMARY KEY (dateid)
);

-------------------------------------------------------

CREATE TABLE public."DimCategory"
(
    categoryid integer NOT NULL,
    category character(50),
    CONSTRAINT "DimCategory_pkey" PRIMARY KEY (categoryid)
);

-------------------------------------------------------

CREATE TABLE public."DimCountry"
(
    countryid integer NOT NULL,
    country character(50),
    CONSTRAINT "DimCountry_pkey" PRIMARY KEY (countryid)
);

-----------------------------------------------------------

CREATE TABLE public."FactSales"
(
    orderid integer NOT NULL,
    dateid integer,
    countryid integer,
    categoryid integer,
    amount integer,
    CONSTRAINT "FactSales_pkey" PRIMARY KEY (orderid)
);

```

## Loading Data
In this exercise you will load the data into the tables. You will load the data provided by the company in csv format.

Note: Ensure that you upload the files to this path: /var/lib/pgadmin/

### Task 1 - Load data into the dimension table DimDate
Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv)

Load the downloaded data into DimDate table.
Take a screenshot of the first 5 rows in the table DimDate.
Name the screenshot DimDate.jpg. (Images can be saved with either the .jpg or .png extension.)
```sql
copy public."DimDate" FROM '/home/project/DimDate.csv' DELIMITER ',' CSV header
```

### Task 2 - Load data into the dimension table DimCategory
Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv)

Load the downloaded data into DimCategory table.
Take a screenshot of the first 5 rows in the table DimCategory.
Name the screenshot DimCategory.jpg. (Images can be saved with either the .jpg or .png extension.)
```sql
copy public."DimCategory" FROM '/home/project/DimCategory.csv' DELIMITER ',' CSV header
```

### Task 3 - Load data into the dimension table DimCountry
Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv)

Load the downloaded data into DimCountry table.
Take a screenshot of the first 5 rows in the table DimCountry.
Name the screenshot DimCountry.jpg. (Images can be saved with either the .jpg or .png extension.)
```sql
copy public."DimCountry" FROM '/home/project/DimCountry.csv' DELIMITER ',' CSV header
```

### Task 4 - Load data into the fact table FactSales
Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv)

Load this data into FactSales table.
Take a screenshot of the first 5 rows in the table FactSales.
Name the screenshot FactSales.jpg. (Images can be saved with either the .jpg or .png extension.)
```sql
copy public."FactSales" FROM '/home/project/FactSales.csv' DELIMITER ',' CSV header
```

## Queries for data analytics
In this exercise you will query the data you have loaded in the previous exercise.

### Task 5 - Create a grouping sets query
Create a grouping sets query using the columns country, category, totalsales.
```sql
SELECT
    c.country,
    ct.category,
    SUM(f.amount) as "totalsales"
FROM
    public."FactSales" f
    INNER JOIN public."DimCountry" c ON f.countryid = c.countryid
    INNER JOIN public."DimCategory" ct ON f.categoryid = ct.categoryid
GROUP BY
    GROUPING SETS (
        (c.country, ct.category)
    )
ORDER BY
    c.country,
    ct.category;

```
Take a screenshot of the sql query and the output rows. Also save the query as a text for later use.
Name the screenshot groupingsets.jpg. (Images can be saved with either the .jpg or .png extension.)

### Task 6 - Create a rollup query
Create a rollup query using the columns year, country, and totalsales.

Take a screenshot of the sql query and the output rows. Also save the query as a text for later use.
Name the screenshot rollup.jpg. (Images can be saved with either the .jpg or .png extension.)

```sql
SELECT
    d.year,
    c.country,
    SUM(f.amount) as "totalsales"
FROM
    public."FactSales" f
    INNER JOIN public."DimDate" d ON f.dateid = d.dateid
    INNER JOIN public."DimCountry" c ON f.countryid = c.countryid
GROUP BY
    ROLLUP (d.year, c.country)
ORDER BY
    d.year DESC,
    c.country;
```

### Task 7 - Create a cube query
Create a cube query using the columns year, country, and average sales.

Take a screenshot of the sql query and the output rows. Also save the query as a text for later use.
Name the screenshot cube.jpg. (Images can be saved with either the .jpg or .png extension.)

```sql
SELECT
    d.year,
    c.country,
    AVG(f.amount) as "average sales"
FROM
    public."FactSales" f
    INNER JOIN public."DimDate" d ON f.dateid = d.dateid
    INNER JOIN public."DimCountry" c ON f.countryid = c.countryid
GROUP BY
    CUBE (d.year, c.country);
```

### Task 8 - Create an MQT
Create an MQT named total_sales_per_country that has the columns country and total_sales.

Take a screenshot of the sql query and the output rows. Also save the query as a text for later use.
Name the screenshot mqt.jpg. (Images can be saved with either the .jpg or .png extension.)

```sql
CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT
    c.country,
    SUM(f.amount) AS total_sales
FROM
    public."FactSales" f
    INNER JOIN public."DimCountry" c ON f.countryid = c.countryid
GROUP BY
    c.country;

REFRESH MATERIALIZED VIEW total_sales_per_country;

SELECT * FROM total_sales_per_country;
```