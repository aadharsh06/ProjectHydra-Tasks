from prometheus_client import start_http_server, Counter, Histogram
from time import sleep

# Metrics
total_req = Counter(
    "finance_api_requests_total",
    "Total requests made to the finance API"
)

error_count = Counter(
    "finance_api_errors_total",
    "Number of failed API calls"
)

res_time = Histogram(
    "finance_api_request_latency_ms",
    "Response time of the server in milliseconds",
    buckets=(50, 100, 200, 500, 1000, 2000)
)

def run():
    while True:
        total_req.inc()
        res_time.observe(120)
        sleep(4)

start_http_server(8600)
run()

