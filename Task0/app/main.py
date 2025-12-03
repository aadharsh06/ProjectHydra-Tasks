
# Fastapi used

from fastapi import FastAPI

app = FastAPI()

# "Has a single /health endpoint returning "OK"."

@app.get ( "/health" )

def health():
    return "OK"
