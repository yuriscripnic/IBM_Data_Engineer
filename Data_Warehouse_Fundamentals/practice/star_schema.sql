DROP TABLE IF EXISTS DimCustomerSegment;

CREATE TABLE
    DimCustomerSegment (
        Segmentid INT PRIMARY KEY,
        City VARCHAR(255) NOT NULL
    );

DROP TABLE IF Exists "DimDate";

CREATE TABLE
    DimDate (
        Dateid INT PRIMARY KEY,
        date DATE NOT NULL,
        Year INT NOT NULL,
        Quarter INT NOT NULL,
        QuarterName VARCHAR(2) NOT NULL,
        Month INT NOT NULL,
        Monthname VARCHAR(255) NOT NULL,
        Day INT NOT NULL,
        Weekday INT NOT NULL,
        WeekdayName VARCHAR(255) NOT NULL
    );

DROP TABLE IF EXISTS DimProduct;

CREATE TABLE
    DimProduct (
        Productid INT PRIMARY KEY,
        Producttype VARCHAR(255) NOT NULL
    );

DROP TABLE IF EXISTS FactSales;

CREATE TABLE
    FactSales (
        Salesid VARCHAR(255) PRIMARY KEY,
        Dateid INT NOT NULL,
        Productid INT NOT NULL,
        Segmentid INT NOT NULL,
        Price_PerUnit DECIMAL(10, 2) NOT NULL,
        QuantitySold INT NOT NULL,
        FOREIGN KEY (Dateid) REFERENCES DimDate (Dateid),
        FOREIGN KEY (Productid) REFERENCES DimProduct (Productid),
        FOREIGN KEY (Segmentid) REFERENCES DimCustomerSegment (Segmentid)
    );