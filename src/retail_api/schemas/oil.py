from datetime import date
from pydantic import BaseModel


class Oil(BaseModel):
    date: date
    dcoilwtico: float | None