from fastapi import APIRouter
from datetime import date

from retail_api.repositories.finance_repository import get_oil_prices

from retail_api.schemas.oil import Oil


router = APIRouter(prefix="/finance", tags=["finance"])


@router.get("/oil", response_model=list[Oil])
def read_oil_prices(
    start_date: date | None = None,
    end_date: date | None = None,
) -> list[Oil]:
    return get_oil_prices(
        start_date,
        end_date,
)