
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import numpy as np
import joblib
import os
from time import time
from collections import deque, Counter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

app = FastAPI()

model = None
scaler = None
FEATURE_NAMES = None

total_req = 0
error_count = 0

all_data = np.array([])
all_y = []

pred_latency = deque ( maxlen = 10000 )

# Input Schema!!

class WineInput ( BaseModel ):
    fixed_acidity: float = Field ( ..., ge = 0 )
    volatile_acidity: float = Field ( ..., ge = 0 )
    citric_acid: float = Field ( ..., ge = 0 )
    residual_sugar: float = Field ( ..., ge = 0 )
    chlorides: float = Field ( ..., ge = 0 )
    free_sulfur_dioxide: float = Field ( ..., ge = 0 )
    total_sulfur_dioxide: float = Field ( ..., ge = 0 )
    density: float = Field ( ..., ge = 0 )
    pH: float = Field ( ..., ge = 0 )
    sulphates: float = Field ( ..., ge = 0 )
    alcohol: float = Field ( ..., ge = 0 )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler ( request: Request, exc: RequestValidationError ):
    global error_count
    error_count += 1

    return JSONResponse ( status_code = 422, content = { "detail": exc.errors() } )

@app.on_event ( "startup" )
def load_model():
    try:
        global model, scaler, FEATURE_NAMES

        model = joblib.load ( "wine_model.pkl" )
        scaler = joblib.load ( "scaler.pkl" )

        FEATURE_NAMES = [
            "fixed_acidity",
            "volatile_acidity",
            "citric_acid",
            "residual_sugar",
            "chlorides",
            "free_sulfur_dioxide",
            "total_sulfur_dioxide",
            "density",
            "pH",
            "sulphates",
            "alcohol",
        ]
    except Exception as e:
        global error_count
        error_count += 1
        raise HTTPException ( status_code = 400, detail = str ( e ) )

@app.get ( "/health" )
def health():
    return "OK"

@app.get ( "/model-info" )
def model_info():
    try:
        return {
            "model_type": type ( model ).__name__,
            "objective": model.get_xgb_params().get ( "objective" ),
            "n_estimators": model.n_estimators,
            "max_depth": model.max_depth,
            "features": FEATURE_NAMES
        }
    except Exception as e:
        global error_count
        error_count += 1
        raise HTTPException ( status_code = 400, detail = str ( e ) )
        
@app.post ( "/predict" )
def predict ( data: WineInput ):
    global pred_latency, all_data, all_y, total_req
    total_req += 1
    try:
        start = time()
        x = np.array ( [ [ getattr ( data, f ) for f in FEATURE_NAMES ] ] )
        x_scaled = scaler.transform ( x )
        pred = model.predict ( x_scaled )[0]
        end = time()
        
        pred_latency.append ( ( end - start ) * 1000 )
        if all_data.size > 0:
            all_data = np.vstack ( [ all_data, x ] )
        else:
            all_data = np.copy ( x )
        
    except Exception as e:
        global error_count
        error_count += 1
        raise HTTPException ( status_code = 400, detail = str ( e ) )
    
    all_y.append ( int ( round ( pred ) ) )
    return {
        "predicted_quality": round ( float ( pred ), 2 ),
        "predicted_quality_rounded": int ( round ( pred ) )
    }

@app.get ( "/metrics" )
def get_metrics():
    global error_count, pred_latency, all_data, all_y, total_req, FEATURE_NAMES

    d = {}
    
    d["Total requests"] = total_req

    if len ( pred_latency ) == 0:
        d["P50_latency_ms"] = 0
        d["P95_latency_ms"] = 0
        d["P99_latency_ms"] = 0
    else:
        d["P50_latency_ms"] = float ( np.percentile ( pred_latency, 50 ) )
        d["P95_latency_ms"] = float ( np.percentile ( pred_latency, 95 ) )
        d["P99_latency_ms"] = float ( np.percentile ( pred_latency, 99 ) )

    d["Error count"] = error_count
        
    if all_data.size > 0:
        for i in range ( len ( FEATURE_NAMES ) ):
            name = FEATURE_NAMES[i]
            d[name + "_min"] = float ( np.min ( all_data[:, i] ) )
            d[name + "_max"] = float ( np.max ( all_data[:, i] ) )
            d[name + "_mean"] = float ( np.mean ( all_data[:, i] ) )

        d["y_min"] = float ( np.min ( all_y ) )
        d["y_max"] = float ( np.max ( all_y ) )
        d["y_mean"] = float ( np.mean ( all_y ) )
    else:
        for i in range ( len ( FEATURE_NAMES ) ):
            name = FEATURE_NAMES[i]
            d[name + "_min"] = None
            d[name + "_max"] = None
            d[name + "_mean"] = None

        d["y_min"] = None
        d["y_max"] = None
        d["y_mean"] = None

    return d

