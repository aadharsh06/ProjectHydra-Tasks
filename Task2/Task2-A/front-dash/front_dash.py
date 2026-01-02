
from requests import get as req_get
from fastapi.responses import HTMLResponse
from time import time
from fastapi import FastAPI
import psutil

total_req = 0
error_count = 0
res_time = 0

data_url = "http://fetch-stock:8000"

def get_data():
    global res_time
    
    try:
        global total_req
        
        res_start = time()
        data = req_get ( data_url )
        res_end = time()

        res_time = res_end - res_start
        
        total_req += 3

        return data.json()
    
    except Exception as e:
        global error_count
        
        res_time = 0
        
        data = ""
        print ( e )
        error_count += 1

        return ""

print ( get_data() )

app = FastAPI()

@app.get ( "/prices" )
def prices():
    return get_data()

@app.get ( "/metrics" )
def metrics():
    cpu = psutil.cpu_percent ( interval = 1 )
    mem = psutil.virtual_memory().percent

    return { 'cpu_usage' : str ( cpu ),
             'mem_usage' : str ( mem ),
             'res_time' : str ( round ( res_time, 5 ) ),
             'total_req' : str ( total_req ),
             'error_count' : str ( error_count )
             }

@app.get ( "/", response_class = HTMLResponse )
def dashboard():
    return """
    <!DOCTYPE html>
<html>
    <head>
        <title>Live Stocks</title>

    </head>
    <body>

    <h1>Live Stock Dashboard</h1>
    <div id="data"></div>

    <script>
    async function loadData() {
        const res = await fetch('/prices');
        const data = await res.json();

        document.getElementById("data").innerHTML =
            Object.entries(data).map(([ticker, arr]) => {
                const price = arr[0];
                const change = arr[1];
                const color = change >= 0 ? "green" : "red";

                return `
                    <div class='stock ${color}'>
                        ${ticker}: ${price} 
                        (Change: ${change})
                    </div>
                `;
            }).join("");
    }

    loadData();
    setInterval(loadData, 5000);
    </script>

    </body>
    </html>
    """




