
# We run this on port 8600

print ( "PYEXP started" )

from prometheus_client import start_http_server, Gauge
from requests import get
from time import sleep

cpu_usage = Gauge ( "cpu_usage", "Percentage of the CPU currently being used" )
mem_usage = Gauge ( "mem_usage", "Percentage of the Memory (RAM) currently being used" )
res_time = Gauge ( "res_time", "Response time of the server, latency, in milliseconds" )
total_req = Gauge ( "total_req", "Total requests made to the finance API" )
error_count = Gauge ( "error_count", "Number of times API called failed" )

# Docker network name, is URL!

hydra_url = "http://front-dash:8080"

def scrape_and_set():
    while True:
        try:

            data = get ( hydra_url + "/metrics" ).json()
            cpu_usage.set ( float (data["cpu_usage"] ) )
            mem_usage.set ( float ( data["mem_usage"] ) )
            res_time.set ( float ( data["res_time"] ) )
            total_req.set ( float ( data["total_req"] ) )
            error_count.set ( float ( data["error_count"] ) )

        except Exception as e:
            print ( "Hydra service not active!! ", e )
            
        sleep ( 4 )

print ( "PYEXP SERVER" )

start_http_server ( 8600 )
scrape_and_set()
