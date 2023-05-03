from fastapi import FastAPI
from src.routes.game import router as game_router

app = FastAPI()

app.include_router(game_router)
