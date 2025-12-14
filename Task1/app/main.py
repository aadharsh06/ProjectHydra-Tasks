
from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get ( "/health" )
def get_health():
    return { "Health" : "200" }
    
@app.get ( "/metrics" )
def get_metrics():
    cpu = randint ( 0, 1000 ) / 10
    mem = randint ( 0, 1000 ) / 10
    res = randint ( 0, 50 )
    return { "cpu_percent" : str ( cpu ), "memory_percent" : str ( mem ), "response_ms" : str ( res ) }

@app.get ( "/simulate_failure" )
def get_fail():
    return { "Health_Fail" : "500" }
