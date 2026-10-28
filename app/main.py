from fastapi import FastAPI

app = FastAPI(
    title="StockSage API",
    description="Inventory intelligence for small retailers",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "StockSage API is running"}