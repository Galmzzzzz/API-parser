from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel, Field

app = FastAPI()


# проверка полей на какие то данные 
class ProductCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


# классы 
class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True



# Базовый гет
@app.get("/items")
def get_items():
    return [{"id": 1, "name": "Book"}]

# использование класса 
@app.post("/items")
def create_item(item: ItemCreate):
    return {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock
    }


# КАКИЕ ТО МЕТОДЫ НЕ ШАРЮ

@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"message": f"item {item_id} updated"}

@app.patch("/items/{item_id}")
def patch_item(item_id: int):
    return {"message": f"item {item_id} partially updated"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"item {item_id} deleted"}

# КАКИЕ ТО МЕТОДЫ НЕ ШАРЮ
