from pydantic import BaseModel

class IWrite(BaseModel):
    name: str
    description: str
