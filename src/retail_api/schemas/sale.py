from datetime import date
from pydantic import BaseModel


class Sale(BaseModel):
    date: date
    store_nbr: int
    family: str
    sales: float
    onpromotion: int