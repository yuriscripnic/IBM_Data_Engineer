# importing libraries
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
#defining DAG arguments
default_args = {
    'owner': 'Dummy',
    'start_date': days_ago(0),
    'email': ['dummy@mail.com'],
    'email': ['dummy@mail.com'],
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

# define the tasks
# Set up the lab environment
# Raw data is stored in a different for organization propose
# Data files aren't in Unix End of Line (\n) , the sed commands remove \r characters 
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command="""mkdir -p /home/project/airflow/dags/finalassignment/data; \
        tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/data""",
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='tr -d "\r" </home/project/airflow/dags/finalassignment/data/vehicle-data.csv | cut -f1-4 -d","  > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command=
    """tr -d "\r" < /home/project/airflow/dags/finalassignment/data/tollplaza-data.tsv | tr "\t" "," | cut -f5-7 -d","  > /home/project/airflow/dags/finalassignment/tsv_data.csv""",
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command=
    """tr -d "\r" < /home/project/airflow/dags/finalassignment/data/payment-data.txt | tr -s '[:space:]'  \
     | cut -f11,12 -d" " | tr " " "," > \
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
         > /home/project/airflow/dags/finalassignment/extracted_data.csv""",
    dag=dag,
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command=
        """paste -d"," <(echo "`cut -f1-3 -d\",\" /home/project/airflow/dags/finalassignment/extracted_data.csv`") \
            <(echo "`cut -f4 -d\",\" /home/project/airflow/dags/finalassignment/extracted_data.csv | tr [:lower:] [:upper:]`") \
            <(echo "`cut -f5- -d\",\" /home/project/airflow/dags/finalassignment/extracted_data.csv`") > /home/project/airflow/dags/finalassignment/transformed_data.csv""",
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data