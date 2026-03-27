import pandas as pd
from datetime import date

from retail_api.core.paths import KAGGLE_DIR


def list_stores() -> list[dict]:
    stores_df = pd.read_csv(KAGGLE_DIR / "stores.csv")
    return stores_df.to_dict(orient="records")


def list_store_by_nbr(store_nbr: int) -> dict | None:
    stores_df = pd.read_csv(KAGGLE_DIR / "stores.csv")
    filtered_df = stores_df[stores_df["store_nbr"] == store_nbr]
    
    if filtered_df.empty:
        return None
    
    return filtered_df.iloc[0].to_dict()


def get_sales(
    start_date: date | None = None,
    end_date: date | None = None,
    store_nbr: int | None= None,
    limit: int=1000
    ) -> list[dict]:
    df = pd.read_csv(KAGGLE_DIR / "train.csv", parse_dates=["date"])
    
    if start_date:
        df = df[df["date"] >= pd.Timestamp(start_date)]
        
    if end_date:
        df = df[df["date"] <= pd.Timestamp(end_date)]
        
    if store_nbr:
        df = df[df["store_nbr"] == store_nbr]
        
    return df.head(limit).to_dict(orient="records")
        