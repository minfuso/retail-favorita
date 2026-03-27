import pandas as pd
from datetime import date

from retail_api.core.paths import KAGGLE_DIR


def list_holidays(
    start_date: date | None = None,
    end_date: date | None = None,
    locale: str | None = None,
    locale_name: str | None = None,
    transferred: bool | None = None,
) -> list[dict]:
    df = pd.read_csv(KAGGLE_DIR / "holidays_events.csv", parse_dates=["date"])
    
    if start_date:
        df = df[df["date"] >= pd.Timestamp(start_date)]
        
    if end_date:
        df = df[df["date"] <= pd.Timestamp(end_date)]
        
    if locale:
        df = df[df["locale"] == locale]
        
    if locale_name:
        df = df[df["locale_name"] == locale_name]
        
    if transferred is not None:
        df = df[df["transferred"] == transferred]
        
    return df.to_dict(orient="records")