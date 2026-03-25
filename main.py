from fastapi import FastAPI
from parser import parser
app = FastAPI()

@app.get("/get-data")
def get_data():
    data = parser()
    return data

@app.post("/parse")
def parse():
    parser()
    return{"status" : "succes"}