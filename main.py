from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "saba7 el gamal"}