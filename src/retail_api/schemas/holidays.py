from datetime import date
from pydantic import BaseModel


class Holidays(BaseModel):
    date: date
    type : str
    locale: str
    locale_name: str
    description: str
    transferred: bool