from nba_api.stats.endpoints import ScoreboardV3
from datetime import date

def get_live_games():
    try:
        today = date.today().strftime("%Y-%m-%d")
        board = ScoreboardV3(game_date=today)
        
        headers = board.game_header.get_data_frame()
        scores = board.line_score.get_data_frame()
        
        result = []
        for _, game in headers.iterrows():
            game_id = game["gameId"]
            teams = scores[scores["gameId"] == game_id]
            
            away = teams.iloc[0]
            home = teams.iloc[1]
            
            result.append({
                "gameId": game_id,
                "status": game["gameStatusText"],
                "homeTeam": {
                    "name": f"{home['teamCity']} {home['teamName']}",
                    "tricode": home["teamTricode"],
                    "score": int(home["score"]) if home["score"] else 0
                },
                "awayTeam": {
                    "name": f"{away['teamCity']} {away['teamName']}",
                    "tricode": away["teamTricode"],
                    "score": int(away["score"]) if away["score"] else 0
                }
            })
        return result
    except Exception as e:
        print(f"Error fetching live games: {e}")
        return []
    

if __name__ == "__main__":
    games = get_live_games()
    for game in games:
        print(game)
