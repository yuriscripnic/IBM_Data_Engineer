# Hands-on Lab: OLTP Database

## Scenario
You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MySQL as an OLTP database. You will be using MySQL to store the OLTP data.

## Objectives
In this assignment you will:
- design the schema for OLTP database.
- load data into OLTP database.
- automate admin tasks.

### Exercises - Setting up the database

#### Exercise 1 - Check the lab environment
- Start MySQL server.

#### Exercise 2 - Design the OLTP Database
##### Task 1 - Create a database.
Create a database named sales.

```sql
create database sales;
```

##### Task 2 - Design a table named sales_data.
Design a table named sales_data based on the sample data given.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/sampledata.png)

- Create the sales_data table in sales database.
- Take a screenshot of the sql statement you used and the output. Also save the code in a text document for later use.
- Name the screenshot as createtable.jpg. (images can be saved with either .jpg or .png extension)

```sql
create table sales_data (
    product_id int,
    customer_id int,
    price numeric(10,2),
    quantity int,
    timestamp date;
);
```


### Exercises - Querying and Admin tasks

#### Exercise 3 - Load the Data

##### Task 3 - Import the data in the file oltpdata.csv

- Download the file oltpdata.csv from [here](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv).

- Import the data from oltpdata.csv into sales_data table using phpMyAdmin.- 
- Take a screenshot of the phpMyAdmin import status.- 
- Name the screenshot as importdata.jpg. (images can be saved with either .jpg or .png extension)

```sql
LOAD DATA
    INFILE '/home/project/oltpdata.csv' 
    INTO TABLE sales_data 
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
```

```bash
mysqlimport --fields-terminated-by=, \
            --lines-terminated-by="\n" \
            --local \
            --user=root \
            --password=aOqGTOC5Uk4Am4FyaCNzGpRv \
             /home/project/oltpdata.csv
```



##### Task 4 - List the tables in the database sales.
- Take a screenshot of the command you used and the output. Also save the code in a text document for later use.
- Name the screenshot as listtables.jpg. (images can be saved with either .jpg or .png extension)

```sql
show tables;
```

##### Task 5. Write a query to find out the count of records in the tables sales_data.
Take a screenshot of the command you used and the output. Also save the code in a text document for later use.
Name the screenshot as salesrows.jpg. (images can be saved with either .jpg or .png extension)

```sql
select count(*) from sales_data;
```

#### Exercise 4 - Set up Admin tasks
##### Task 6 - Create an index
- Create an index named ts on the timestamp field.
```sql
create index ts on sales_data (`col 5`)
```

##### Task 7 - List indexes
- List indexes on the table sales_data.
- Take a screenshot of the command you used and the output. Also save the code in a text document for later use.
- Name the screenshot as listindexes.jpg. (images can be saved with either .jpg or .png extension)
```sql
show indexes from sales_data;
```

##### Task 8 - Write a bash script to export data.
- Write a bash script named datadump.sh that exports all the rows in the sales_data table to a file named sales_data.sql
- Take a screenshot of the contents of the datadump.sh bash file command you used and the output. Also save the code in a text document for later use.
- Name the screenshot as exportdata.jpg. (images can be saved with either .jpg or .png extension)

```bash
#!/bin/bash

mysqldump --host=172.21.18.194 --port=3306 --user=root \
    --password=aOqGTOC5Uk4Am4FyaCNzGpRv \
    sales sales_data > sales_data.sql
```





