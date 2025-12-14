
# We run this on port 8600

from prometheus_client import start_http_server, Gauge
from requests import get
from time import sleep

# According to the task, we have to scrape all endpoints, but expose only metrics

health = Gauge ( "Health", "Current health of the server" )

cpu_percent = Gauge ( "cpu_percent", "Percentage of the CPU currently being used" )
memory_percent = Gauge ( "mem_percent", "Percentage of the Memory (RAM) currently being used" )
response_ms = Gauge ( "response_ms", "Response time of the server, latency, in milliseconds" )

sim_fail = Gauge ( "Health_Fail", "Simulated Failure of the server" )

# Docker network name, is URL!

hydra_url = "http://hydrabase:8080"

def scrape_and_set():
    while True:
        try:
            data = get ( hydra_url + "/health" ).json()
            #health.set ( data["Health"] )

            data = get ( hydra_url + "/metrics" ).json()
            cpu_percent.set ( data["cpu_percent"] )
            memory_percent.set ( data["memory_percent"] )
            response_ms.set ( data["response_ms"] )

            data = get ( hydra_url + "/simulate_failure" ).json()
            #sim_fail.set ( data["Health_Fail"] )

        except Exception as e:
            print ( "Hydra service not active!! ", e )
            
        sleep ( 10 )

start_http_server ( 8600 )
scrape_and_set()
            
