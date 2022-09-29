from pydantic import BaseModel


class Item(BaseModel):
    """Contract for item"""

    name: str
    age: int
    salary: float
