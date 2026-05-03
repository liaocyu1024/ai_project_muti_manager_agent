from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Project Manager")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Project Manager Running"}
