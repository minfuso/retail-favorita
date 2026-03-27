from fastapi import APIRouter, HTTPException
from typing import Optional
from datetime import date

from retail_api.repositories.retail_repository import list_stores, list_store_by_nbr, get_sales
from retail_api.schemas.store import Store
from retail_api.schemas.sale import Sale

router = APIRouter(prefix="/retail", tags=["retail"])


@router.get("/stores", response_model=list[Store])
def read_stores() -> list[Store]:
    return list_stores()


@router.get("/stores/{store_nbr}", response_model=Store)
def read_store_by_nbr(store_nbr: int) -> dict:
    store = list_store_by_nbr(store_nbr)
    
    if store is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Store {store_nbr} not found"
        )
        
    return store


@router.get("/sales", response_model=list[Sale])
def read_sales(
    start_date: Optional[date] = None, 
    end_date: Optional[date] = None, 
    store_nbr: Optional[int] = None,
    limit: int = 1000
) -> list[dict]:
    return get_sales(
        start_date,
        end_date, 
        store_nbr,
        limit=limit,
    )
