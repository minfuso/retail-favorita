from fastapi import APIRouter
from typing import Optional
from datetime import date

from retail_api.repositories.government_repository import list_holidays 
from retail_api.schemas.holidays import Holidays


router = APIRouter(prefix="/government", tags=["government"])

@router.get("/holidays", response_model=list[Holidays])
def read_holidays(
    start_date: Optional[date] = None, 
    end_date: Optional[date] = None, 
    locale: Optional[str] = None,
    locale_name: Optional[str] = None,
    transferred: Optional[bool] = None
) -> list[dict]:
    return list_holidays(
        start_date,
        end_date,
        locale,
        locale_name,
        transferred,
    )