# ETL and Data Pipelines with Shell, Airflow and Kafka, Final Project Overview

## Instructions
Now that you are equipped with the knowledge and skills to extract, transform and load data you will use these skills to perform ETL, create a pipeline and upload the data into a database. You will use BashOperator with Airflow in the hands-on lab.

## Scenario
You are a data engineer at a data analytics consulting company. You have been assigned a project to decongest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setup that uses different file formats. Your job is to collect data available in different formats and consolidate it into a single file.

In this assignment, you will develop an Apache Airflow DAG that will:

- Extract data from a csv file
- Extract data from a tsv file
- Extract data from a fixed-width file
- Transform the data
- Load the transformed data into the staging area

## Exercise 1: Create imports, DAG argument and definition
- Task 1.1: Define DAG arguments (2 pts)
- Task 1.2: Define the DAG (2 pts)

## Exercise 2: Create the tasks using BashOperator
- Task 2.1: Create a task to unzip data. (2 pts)
- Task 2.2: Create a task to extract data from csv file (2 pts)
- Task 2.3: Create a task to extract data from tsv file (2 pts)
- Task 2.4: Create a task to extract data from fixed width file (2 pts)
- Task 2.5: Create a task to consolidate data extracted from previous tasks (2 pts)
- Task 2.6: Transform the data (2 pts)
- Task 2.7: Define the task pipeline (1 pt)

## Exercise 3: Getting the DAG operational
- Task 3.1: Submit the DAG (1 pt)
- Task3.2: Unpause and trigger the DAG (3 pts)
- Task 3.3: List the DAG tasks (2 pts)
- Task 3.4: Monitor the DAG (2 pts)