# import the libraries
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# defining DAG arguments
default_args = {
    'owner': 'Dummy',
    'start_date': days_ago(0),
    'email': ['dummy@mail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# define the path to the data directory
path = "/home/project/airflow/dags/finalassignment"

# define the tasks

# Task 1: Unzip data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command=f"mkdir -p {path}/data; tar -xvf {path}/tolldata.tgz -C {path}/data",
    dag=dag,
)

# Task 2: Extract data from csv
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command=f'tr -d "\r" < {path}/data/vehicle-data.csv | cut -f1-4 -d"," > {path}/csv_data.csv',
    dag=dag,
)

# Task 3: Extract data from tsv
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command=f'tr -d "\r" < {path}/data/tollplaza-data.tsv | tr "\\t" "," | cut -f5-7 -d"," > {path}/tsv_data.csv',
    dag=dag,
)

# Task 4: Extract data from fixed width file
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command=f'tr -d "\r" < {path}/data/payment-data.txt | tr -s "[:space:]" | cut -d" " -f11,12 | tr " " "," > {path}/fixed_width_data.csv',
    dag=dag,
)

# Task 5: Consolidate data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=f'paste -d"," {path}/csv_data.csv {path}/tsv_data.csv {path}/fixed_width_data.csv > {path}/extracted_data.csv',
    dag=dag,
)

# Task 6: Transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command=f"awk -F, 'BEGIN {{OFS=FS}} {{$4=toupper($4)}} 1' {path}/extracted_data.csv > {path}/transformed_data.csv",
    dag=dag,
)

# task pipeline
unzip_data >> [extract_data_from_csv, extract_data_from_tsv, extract_data_from_fixed_width] >> consolidate_data >> transform_data