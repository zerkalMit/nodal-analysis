import src.routes as rts
import uvicorn
from fastapi import FastAPI

app = FastAPI()

app.include_router(rts.main_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8003)
