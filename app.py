import os
import logging
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message": "backend is running"}

@app.get("/hello")
def hello():
    return {"message": "Hello from backend"}

@app.get("/time")
def time():
    return {"current_time": str(datetime.now())}

@app.get("/health")
def health():
    logger.info("Health check called")
    return {
        "status": "ok",
        "app": os.getenv("APP_NAME", "devops-backend"),
        "env": os.getenv("ENV", "development")
    }

@app.get("/crash")
def crash():
    logger.error("crash endpoint called - app will exit")
    raise SystemExit("simulated crash")
