from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.buildings import router as buildings_router

app = FastAPI(title="Buildings API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(buildings_router)

    # добавить тесты времени и через асинхронность 
    # app.diagrams.net
    # что будет если сделать запрос асинк и потом перейти на другую страницу
    # вебхуки 
    # asgi wsgi
    # rest, websocket
    # how promise works
    # serialization in fast api
   