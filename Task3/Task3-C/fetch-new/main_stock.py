
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
    except Exception as e: 
        print ( e )
        for i in stock_list:
            d[i] = ( 0, 0 )
        
    return d

@app.get ( "/" )
def get_stock():
    return get_data()
