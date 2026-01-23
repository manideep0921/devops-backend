FROM python:3.10

WORKDIR /app

COPY app.py .

RUN pip install fastapi uvicorn

CMD ["python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

