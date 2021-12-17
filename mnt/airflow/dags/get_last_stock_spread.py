import pandas as pd
from datetime import date, timedelta

LOCAL_DIR = 'tmp/data/' + str(date.today() - timedelta(days=1))

def main():
    """ Function that calculates the stock's spreading value.
    Formula: spread = high value - low value
    """

    apple_data = pd.read_csv(LOCAL_DIR + "/AAPL_data.csv").sort_values(by = "Datetime", ascending = False)
    tesla_data = pd.read_csv(LOCAL_DIR + "/TSLA_data.csv").sort_values(by = "Datetime", ascending = False)
    spread = [apple_data['High'][0] - apple_data['Low'][0], tesla_data['High'][0] - tesla_data['Low'][0]]
    return spread

if __name__ == '__main__':
    "dags/get_last_stock_spread.py"