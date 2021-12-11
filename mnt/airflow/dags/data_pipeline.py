"""
YOUR DATA PIPELINE GOES HERE
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import date, datetime, timedelta

import get_last_stock_spread
import download_stock_data

default_args = {
            "owner": "airflow",
            "start_date": datetime(2021, 3, 24),
            "depends_on_past": False,
            "email_on_failure": False,
            "retries": 2, # retry twice
            "retry_delay": timedelta(minutes=5) # five minutes interval
        }

with DAG(dag_id="marketvol",
         schedule_interval="6 0 * * 1-5", # running at 6pm for weekdays
         default_args=default_args,
         description='source Apple and Tesla data' ) as dag:

    task_0 = BashOperator(
        task_id="task_0",
        bash_command='''mkdir -p /tmp/data/''' + str(date.today()) #naming the folder with the current day
    )

    task_1 = PythonOperator(
        task_id="task_1",
        python_callable= download_stock_data.main,
        provide_context= True,
        op_kwargs={'stock_name': 'AAPL'}
    )

    task_2 = PythonOperator(
        task_id="task_1",
        python_callable= download_stock_data.main,
        provide_context= True,
        op_kwargs={'stock_name': 'TSLA'}
    )

    task_3 = BashOperator(
        task_id="task_3", 
        bash_command='''mv AAPL_data.csv /tmp/data/'''+ str(date.today())
    )

    task_4 = BashOperator(
        task_id="task_4", 
        bash_command='''mv TSLA_data.csv /tmp/data/'''+ str(date.today())
    )

    task_5 = PythonOperator(
        task_id="task_5",
        python_callable=get_last_stock_spread.main,
    )

task_0>>[task_1,task_2]
task_1>>task_3
task_2>>task_4
[task_3,task_4]>>task_5
