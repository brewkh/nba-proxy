from fastapi import FastAPI

app = FastAPI(title="NBA Data Proxy", version="1.1.0")

@app.get("/health")
def health():
    return {"ok": True, "service": "nba-proxy"}

@app.get("/schedule/today")
def schedule_today():
    # TODO: implement Brisbane-day schedule
    return {"games": []}

@app.get("/injuries")
def injuries():
    # TODO: implement official injury report aggregation
    return {"injuries": []}

@app.get("/lineups/today")
def lineups_today():
    # TODO: implement projected/confirmed starters (+minutes)
    return {"lineups": []}

@app.get("/players/season_summaries_regular")
def season_summaries_regular(season: str, fallback_prior: bool = True):
    # TODO: implement regular-season per-player averages
    return {"season": season, "players": []}

@app.get("/players/game_logs_regular")
def game_logs_regular(player_id: str, last_n: int = 15, include_seasons_back: int = 2):
    # TODO: implement cross-season last-N (regular-season only)
    return {"player_id": player_id, "games": []}
