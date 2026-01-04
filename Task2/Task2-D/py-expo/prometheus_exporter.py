
# We run this on port 8600

from prometheus_client import start_http_server, Gauge
from requests import get
from time import sleep

total_req = Gauge ( "total_requests", "Total requests" )
P50 = Gauge ( "P50_ms", "Latency P50 in ms" )
error_count = Gauge ( "Error_Count", "Error count" )
so2_mean = Gauge ( "So2_Mean", "So2 Mean" )
ph_mean = Gauge ( "pH_Mean", "pH Mean" )
y_mean = Gauge ( "y_mean", "Output Mean" )

# Docker network name, is URL!

hydra_url = "http://model:8080"

def scrape_and_set():
    while True:
        try:
            data = get ( hydra_url + "/metrics" ).json()
            total_req.set ( float ( data["Total requests"] ) )
            P50.set ( float ( data["P50_latency_ms"] ) )
            error_count.set ( float ( data["Error count"] ) )
            so2_mean.set ( float ( data["free_sulfur_dioxide_mean"] ) )
            ph_mean.set ( float ( data["pH_mean"] ) )
            y_mean.set ( float ( data["y_mean"] ) )

        except Exception as e:
            print ( "Hydra service not active!! ", e )
            
        sleep ( 4 )

start_http_server ( 8600 )
scrape_and_set()
