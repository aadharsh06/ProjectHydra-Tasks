FROM python:3.11
COPY . .
RUN pip install fastapi uvicorn requests psutil
CMD [ "uvicorn", "front_dash:app", "--host", "0.0.0.0", "--port", "8080" ]
