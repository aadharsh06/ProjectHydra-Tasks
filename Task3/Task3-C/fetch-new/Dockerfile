FROM python:3.11

RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    wget \
    dnsutils \
    iproute2 \
    net-tools \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN update-ca-certificates

RUN pip install fastapi uvicorn yfinance requests

CMD ["uvicorn", "main_stock:app", "--host", "0.0.0.0", "--port", "8000" ]

