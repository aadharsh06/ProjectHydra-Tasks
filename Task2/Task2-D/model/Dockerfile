FROM python:3.11
COPY . .
RUN pip install fastapi uvicorn requests psutil joblib pydantic typing numpy xgboost scikit-learn
CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080" ]
