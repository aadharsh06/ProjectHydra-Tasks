FROM python:3.11
COPY . .
RUN pip install prometheus-client requests
CMD [ "python3", "-u", "prometheus_exporter.py" ]
