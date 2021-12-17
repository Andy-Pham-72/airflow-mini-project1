# Airflow project!

![Screen Shot 2021-12-17 at 12 29 41 AM](https://user-images.githubusercontent.com/70767722/146494463-25db01b5-0a04-4ef6-a6f5-b20e4278cd47.png)

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

We'll work with 2 stocks symbols: [`AAPL`](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/mnt/airflow/tmp/data/2021-12-16/AAPL_data.csv) and [`TSLA`](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/mnt/airflow/tmp/data/2021-12-16/TSLA_data.csv). The workflow can be seen in [data_pipeline.py](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/mnt/airflow/dags/data_pipeline.py) which is scheduled to run at 6pm on every weekday (Mon - Fri) with the below functions:

- Download the daily price data with one minute interval for the two symbols. Each symbol will have a separate task, Task1 (t1) and Task2 (t2), which run independently and in parallel.
- Save both datasets into CSV files and load them into a directory. Each symbol will have a separate task, Task3 (t3) and Task4 (t4), which run independently and in parallel.
- Run your custom query on the downloaded dataset for both symbols, Task5 (t5). Before this step executes, all previous tasks must complete.

![Screen Shot 2021-12-17 at 12 29 28 AM](https://user-images.githubusercontent.com/70767722/146494411-a9ae5a15-e154-4068-a2fa-032831e0cfd9.png)

**All the tasks should be successfully executed like this:**

![Screen Shot 2021-12-16 at 11 45 15 PM](https://user-images.githubusercontent.com/70767722/146494339-9b02a69b-eb34-4f14-86b6-0f051b5058ea.png)

**We can check all the tasks log in this [folder](https://github.com/Andy-Pham-72/airflow-mini-project1/tree/master/mnt/airflow/logs/marketvol)**

Example of task 5's successful execution log file which gives us a list as an output (checking [get_last_stock_spread.py](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/mnt/airflow/dags/get_last_stock_spread.py) for your reference):

![Screen Shot 2021-12-17 at 12 07 35 PM](https://user-images.githubusercontent.com/70767722/146582104-6ec1cd61-9e3d-4401-9b88-27f70e0f424c.png)

## Steps to follow to execute all files:

1, From Bash shell, execute [`./start.sh`](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/start.sh) and it will build and start all the services.

2, Wait untill all the services are completely executed and they should be healthy as screenshot below:

![Screen Shot 2021-12-17 at 12 31 13 AM](https://user-images.githubusercontent.com/70767722/146494230-c63765d3-6bfb-4162-83a9-1ed378fba5b8.png)

3, Go to `localhost:8080` to access the web ui.

4, Login with username: airflow and password: airflow.

5, Now we can wait for all the tasks running as the schedule or manually trigger the tasks to see the output.

6, After completing all the tasks, we can execute [`./stop.sh`](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/stop.sh) to stop the services.

7, Execute [`./reset.sh`](https://github.com/Andy-Pham-72/airflow-mini-project1/blob/master/reset.sh) to wipe out all the images.

## Future works:
- Integrate CeleryExecutor in the `airflow.cfg` and adjust `docker-compose.yml` configs accordingly.
- The execution of the airflow service in the docker should be utilized since it still takes quiet longer time to be successfully implemented.
