
FROM python:3.11

WORKDIR /app
COPY app/ app/

RUN pip install fastapi uvicorn
CMD ["uvicorn", "app.main:app" ]
