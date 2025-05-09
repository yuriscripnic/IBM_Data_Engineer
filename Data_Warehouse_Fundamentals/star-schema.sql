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

DROP TABLE IF EXISTS DimTruck;

CREATE TABLE
    DimTruck (
        truckid INT PRIMARY KEY,
        truckType VARCHAR(255) NOT NULL
    );

DROP TABLE IF EXISTS DimStation;

CREATE TABLE
    DimStation (
        stationid INT PRIMARY KEY,
        city VARCHAR(255) NOT NULL
    );

DROP TABLE IF EXISTS FactTrips;

CREATE TABLE
    FactTrips (
        tripid INT PRIMARY KEY,
        dateid INT REFERENCES DimDate (dateid),
        stationid INT REFERENCES DimStation (stationid),
        truckid INT REFERENCES DimTruck (truckid),
        wastecollected DECIMAL(10, 2) NOT NULL        
    );