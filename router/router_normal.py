from fastapi import APIRouter 
from input_interface.normal_input_interface import ItemA

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/add")
def add_numbers(a: int, b: int):
    result = a + b 
    return {
        "result": result
        }

@router.post("/items")
def create_item(item: ItemA):
    return {"item_name": item.name, "item_price": item.price, "item_offer": item.is_offer}

@router.get("/items")
def create_item(a: int):
    return {"item_name": a}