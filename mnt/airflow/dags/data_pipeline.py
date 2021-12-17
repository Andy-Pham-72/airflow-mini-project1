"""
YOUR DATA PIPELINE GOES HERE
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import date, datetime, timedelta

import get_last_stock_spread
import download_stock_data

today_var = datetime.today() - timedelta(days=1) # convert from the UTC timezone to EST timezone

default_args = {
            "owner": "airflow",
            "start_date": today_var,
            "depends_on_past": False,
            "email_on_failure": False,
            "retries": 2, # retry twice
            "retry_delay": timedelta(minutes=5) # five minutes interval
        }

with DAG(dag_id="marketvol",
         schedule_interval="6 0 * * 1-5", # 6 0 * * 1-5 running at 6pm for weekdays
         default_args=default_args,
         description='source Apple and Tesla data' ) as dag:

    task_0 = BashOperator(
        task_id="task_0",
        bash_command='''mkdir -p $AIRFLOW_HOME/tmp/data/''' + str(today_var) #naming the folder with the current day
    )

    task_1 = PythonOperator(
        task_id="task_1",
        python_callable= download_stock_data.main,
        provide_context= True,
        op_kwargs={'stock_name': 'AAPL'}
    )

    task_2 = PythonOperator(
        task_id="task_2",
        python_callable= download_stock_data.main,
        provide_context= True,
        op_kwargs={'stock_name': 'TSLA'}
    )

    task_3 = BashOperator(
        task_id="task_3",
        bash_command='''mv $AIRFLOW_HOME/AAPL_data.csv $AIRFLOW_HOME/tmp/data/'''+ str(date.today()- timedelta(days=1))
    )

    task_4 = BashOperator(
        task_id="task_4",
        bash_command='''mv $AIRFLOW_HOME/TSLA_data.csv $AIRFLOW_HOME/tmp/data/'''+ str(date.today()- timedelta(days=1))
    )

    task_5 = PythonOperator(
        task_id="task_5",
        python_callable=get_last_stock_spread.main,
    )

task_0>>[task_1,task_2]
task_1>>task_3
task_2>>task_4
[task_3,task_4]>>task_5
