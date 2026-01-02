FROM python:3.11
COPY . .
RUN pip install fastapi uvicorn yfinance
CMD [ "uvicorn", "main_stock:app", "--host", "0.0.0.0", "--port", "8000" ]
