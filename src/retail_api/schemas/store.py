from pydantic import BaseModel


class Store(BaseModel):
    store_nbr: int
    city: str
    state: str
    type: str
    cluster: int