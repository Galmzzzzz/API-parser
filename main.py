from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from parser import parser
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Buildings API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-data")
def get_data():
    try:
        data = parser()
        return data
    except Exception as e:
        logger.exception("Failed to get data")
        raise HTTPException(status_code=500, detail="Failed to get data") from e

@app.post("/parse")
def run_parser():
    try:
        parser()
        return {"status": "success"}
    except Exception as e:
        logger.exception("Failed to parse data")
        raise HTTPException(status_code=500, detail="Failed to parse data") from e
    

    # добавить тесты времени и через асинхронность 
    # app.diagrams.net
    # что будет если сделать запрос асинк и потом перейти на другую страницу
    # вебхуки 
    # asgi wsgi
    # rest, websocket
    # how promise works
    # serialization in fast api
   