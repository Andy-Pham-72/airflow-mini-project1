from datetime import date, timedelta
import yfinance as yf

def main(stock_name, **kwargs):
    '''
    function downloads the stock from Yahoo Finance with the parameter "stock_name"
    which define the particular stock we want to download.
    for example: "AAPL" for Apple stock or "TSLA" for Tesla stock
    '''

    start_date = date.today()
    end_date = start_date + timedelta(days=1)
    df = yf.download(stock_name, start=start_date, end=end_date, interval='1m')
    df.to_csv(stock_name + "_data.csv", header=False)

if __name__ == '__main__':
    "dags/download_stock_data.py"