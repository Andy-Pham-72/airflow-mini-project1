import pandas as pd
from datetime import date

LOCAL_DIR = 'tmp/data/' + str(date.today())

def main():
    """ Function that calculates the stock's spreading value.
    Formula: spread = high value - low value
    """

    apple_data = pd.read_csv(LOCAL_DIR + "AAPL_data.csv").sort_values(by = "date time", ascending = False)
    tesla_data = pd.read_csv(LOCAL_DIR + "TSLA_data.csv").sort_values(by = "date time", ascending = False)
    spread = [apple_data['high'][0] - apple_data['low'][0], tesla_data['high'][0] - tesla_data['low'][0]]
    return spread

if __name__ == '__main__':
    "dags/get_last_stock_spread.py"