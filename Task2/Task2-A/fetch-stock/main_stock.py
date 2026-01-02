
import yfinance as yf
from fastapi import FastAPI

app = FastAPI()

stock_list = [ "RELIANCE.NS", "TCS.NS", "INFY.NS", "AMZN", "ORCL", "GOOGL" ]

def get_data():
    d = {}

    try:
        for i in stock_list:
            info = yf.Ticker ( i ).info
            d[i] = ( info['currentPrice'],  round ( info["regularMarketPreviousClose"] - info['currentPrice'], 2 ) )
    except: 
        pass

    return d

@app.get ( "/" )
def get_stock():
    return get_data()
