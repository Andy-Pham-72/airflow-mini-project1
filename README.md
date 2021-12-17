# Airflow project

## Project Objectives:

* Incorporate [Docker](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/docker-compose.yml) in order to solve the sharing and reproducing challenges (different operating systems, versioning, lack of process).
* Use Apache Airflow to orchestrate the pipeline.
* Exercise [DAG creation](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/mnt/airflow/dags/data_pipeline.py).
* Use Various Airflow operators like `BashOperator` and `PythonOpertor`.
* Set up the order operation of each task.

In this project, I created a data pipeline to extract online stock market data and deliver future analytical results. Yahoo Finance is used as the data source via the `yfinance` python library.

the [source data](https://github.com/Andy-Pham-72/airflow-mini-project1/tree/master/mnt/airflow/tmp/data) follow this schema:

|    Columns        |  Type                                        |
|-------------------|-----------------------------------------------------|
|Datetime   | STRING                                 |   
|Open        | DECIMAL                                  |   
|High          | DECIMAL (highest price within the time interval)                                       |
|Low   | DECIMAL (lowest price within the time interval)                            |
|Close       | DECIMAL (the last price of the time interval)                             |
|Adj Close    | DECIMAL                             |
|Volume | DECIMAL                              |

We'll work with 2 stocks symbols: `AAPL` and `TSLA`. The workflow can be seen in [data_pipeline.py](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/mnt/airflow/dags/data_pipeline.py) which is scheduled to run at 6pm on every weekday (Mon - Fri) with the below functions:

- Download the daily price data with one minute interval for the two symbols. Each symbol will have a separate task, Task1 (t1) and Task2 (t2), which run independently and in parallel.
- Save both datasets into CSV files and load them into HDFS. Each symbol will have a separate task, Task3 (t3) and Task4 (t4), which run independently and in parallel.
- Run your custom query on the downloaded dataset for both symbols, Task5 (t5). Before this step executes, all previous tasks must complete.

All the tasks should be successfully executed like this:
[pic]

## Steps to follow to execute all files:

1, From Bash shell, execute `./start.sh` and it will build and start all the services.

2, Wait untill all the services are completely executed and they should be healthy as screenshot below:
[pic]

3, Go to `localhost:8080` to access the web ui.

4, Login with username: airflow and password: airflow.

5, Now we can wait for all the tasks running as the schedule or manually trigger the tasks to see the output.

6, After completing all the tasks, we can execute `./stop.sh` to stop the services.

7, Execute `./stop.sh` to wipe out all the images.

