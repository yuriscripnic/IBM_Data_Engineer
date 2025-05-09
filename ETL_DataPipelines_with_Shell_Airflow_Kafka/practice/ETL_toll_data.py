# importing libraries
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
#defining DAG arguments
default_args = {
    'owner': 'YSS',
    'start_date': days_ago(0),
    'email': ['yuriscripnic@gmail.com'],
    'email': ['yuriscripnic@gmail.com'],
    'email': ['yuriscripnic@gmail.com'],
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

# define the tasks
# Set up the lab environment
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/data',
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -f1-4 -d"," /home/project/airflow/dags/finalassignment/data/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command=
    """tr "\t" "," < /home/project/airflow/dags/finalassignment/data/tollplaza-data.tsv \
     | cut -f5-7 -d","  > /home/project/airflow/dags/finalassignment/tsv_data.csv""",
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command=
    """tr -s '[:space:]' < /home/project/airflow/dags/finalassignment/data/payment-data.txt \
     | cut -f10,11 -d" " | tr " " "," > \
     /home/project/airflow/dags/finalassignment/fixed_width_data.csv""",
    dag=dag,
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=
        """paste -d"," \
        /home/project/airflow/dags/finalassignment/csv_data.csv \
        /home/project/airflow/dags/finalassignment/tsv_data.csv \
        /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
         > /home/project/airflow/dags/finalassignment/extracted_data.csv """,
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data
