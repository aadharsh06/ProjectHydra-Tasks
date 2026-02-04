FROM python:3.11
COPY . .
RUN pip install prometheus-client requests
EXPOSE 8600
CMD [ "python3", "-u", "prometheus_exporter.py" ]
