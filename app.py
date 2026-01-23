from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "backend is running"}

@app.get("/hello")
def hello():
    return {"message": "Hello from backend"}

@app.get("/time")
def time():
    return {"current_time": str(datetime.now())}

@app.get("/name")
def my_name():
    return {"name": "Manideep"}
