DROP TABLE IF Exists public."MyDimDate";

CREATE TABLE public."MyDimDate"(
    dateid integer NOT NULL,
    day integer NOT NULL,
    weekday integer NOT NULL,
    weekdayname "char" NOT NULL,
    year integer NOT NULL,
    month integer NOT NULL,
    monthname "char" NOT NULL,
    PRIMARY KEY (dateid)
);