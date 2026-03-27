from fastapi import FastAPI

from retail_api.api.routes.health import router as health_router
from retail_api.api.routes.retail import router as retail_router
from retail_api.api.routes.finance import router as finance_router
from retail_api.api.routes.government import router as government_router

app = FastAPI(title="Retail Favorita API", version="1.0.0")

app.include_router(health_router, prefix="")
app.include_router(retail_router)
app.include_router(finance_router)
app.include_router(government_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Retail Favorita API is running."}