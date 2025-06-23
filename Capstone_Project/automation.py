# import the libraries
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# define the path to the data directory
path = "/home/project/airflow/dags/capstone"

"""
Exercise 2 - Create a DAG
Task 1 - Define the DAG arguments
Create a DAG with these arguments.
- owner
- start_date
- email
- You may define any suitable additional arguments.

Take a screenshot of the code you used clearly showing the above arguments. Also save the code as text spearately for later use.
Name the screenshot dag_args.jpg. (Images can be saved with either the .jpg or .png extension.)
"""

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

"""
Task 2 - Define the DAG
Create a DAG named process_web_log that runs daily.
Use suitable description.
Take a screenshot of the code you used to define the DAG. Also save the code as text spearately for later use.
Name the screenshot dag_definition.jpg. (Images can be saved with either the .jpg or .png extension.)
"""
dag = DAG(
    dag_id='ETL',
    default_args=default_args,
    description='Capstone Project',
    schedule_interval=timedelta(days=1),
)


"""
Task 3 - Create a Task to extract data
Create a Task named extract_data.
This Task should extract the ipaddress field from the web server log file and save it into a file named extracted_data.txt
Take a screenshot of the Task code. Also save the code as text spearately for later use.
Name the screenshot extract_data.jpg. (Images can be saved with either the .jpg or .png extension.)

Data sample
83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:43 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1" 200 171717 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:47 +0000] "GET /presentations/logstash-monitorama-2013/plugin/highlight/highlight.js HTTP/1.1" 200 26185 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149
"""

extract_data = BashOperator(
    task_id='extract_data',
    bash_command=f'cut -d" " -f1 {path}/accesslog.txt > {path}/extracted_data.txt',
    dag=dag,
)


"""
Task 4 - Create a Task to transform the data in the txt file
Create a Task named transform_data.
This Task should filter out all the occurrences of ipaddress “198.46.149.143” from extracted_data.txt and save the output to a file named transformed_data.txt.
Take a screenshot of the Task code. Also save the code as text spearately for later use.
Name the screenshot transform_data.jpg. (Images can be saved with either the .jpg or .png extension.)
"""
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v "198.46.149.143" extracted_data.txt > transformed_data.txt',
    dag=dag,
)

"""
Task 5 - Create a Task to load the data
Create a Task named load_data.
This Task should archive the file transformed_data.txt into a tar file named weblog.tar.
Take a screenshot of the Task code. Also save the code as text spearately for later use.
Name the screenshot load_data.jpg. (Images can be saved with either the .jpg or .png extension.)
"""

load_data = BashOperator(
    task_id='load_data',
    bash_command=f'tar -cvf {path}/weblog.tar {path}/transformed_data.txt',
    dag=dag,
)

"""
Task 6 - Define the Task pipeline
Define the Task pipeline as per the details given below:

- Task	Functionality
- First task	extract_data
- Second task	transform_data
- Third task	load_data
- Take a screenshot of the Task pipeline section of the DAG.
- Name the screenshot pipeline.jpg. (Images can be saved with either the .jpg or .png extension.)
"""
# Define task dependencies
extract_data >> transform_data >> load_data