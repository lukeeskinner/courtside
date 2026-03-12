from fastapi import FastAPI
from nba import get_live_games

app = FastAPI()

@app.get("/games/live")
def live_games():
    return get_live_games()