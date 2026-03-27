import pandas as pd
from datetime import date

from retail_api.core.paths import KAGGLE_DIR


def get_oil_prices(
    start_date: date | None = None,
    end_date: date | None = None,
    ) -> list[dict]:
    df = pd.read_csv(KAGGLE_DIR / "oil.csv", parse_dates=["date"])
    
    if start_date:
        df = df[df["date"] >= pd.Timestamp(start_date)]
        
    if end_date:
        df = df[df["date"] <= pd.Timestamp(end_date)]
        
    return df.to_dict(orient="records")