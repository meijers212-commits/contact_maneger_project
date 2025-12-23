from fastapi import FastAPI
from app.api import router


app = FastAPI()
app.include_router(router, tags="CONTACT_MANEGER", prefix="/home")






if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)