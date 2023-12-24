from pydantic import BaseModel


class ItemA(BaseModel):
    name: str
    price: float
    is_offer: bool = None