from fastapi import FastAPI
from mangum import Mangum
from app.services.electric.import_check import MESSAGE

app = FastAPI()

@app.get("/")
async def root():
    return { 'message' : MESSAGE }

handler = Mangum(app=app)