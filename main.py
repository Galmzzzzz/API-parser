from fastapi import FastAPI
from parser import parser
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # адрес фронта
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get-data")
def get_data():
    data = parser()
    return data

@app.post("/parse")
def parse():
    parser()
    return{"status" : "succes"}