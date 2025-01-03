import utils
import os

os.makedirs("data", exist_ok=True)

config = {
    "games_path" : "data/games.csv",
    "remarks_path" : "data/remarks.csv",
    "runs_path" : "data/runs.csv",
    "config_path" : "data/config.json"
}

game_col = ['id', 'title', 'developer', 'platform']
run_col = ['id', 'game_id', 'state', 'score']
remark_col = ['id', 'run_id', 'text']

game = {
    "id" : 1,
    "title" : "Mushihimesama",
    "developer" : "cave",
    "platform" : "Steam"
}

run = {
    "id" : 1,
    "game_id" : game["id"],
    "state" : False,
    "score": 1000000,
    "stage" : 3
}

remark_1 = {
    "id" : 1,
    "run_id" : run["id"],
    "text" : "This was another fail at stage 3"
}

remark_2 = {
    "id" : 2,
    "run_id" : run["id"],
    "text" : "I hate this game"

}

games = []
games.append(game_col)
games.append(list(game.values()))
utils.save_csv(config["games_path"], games)

runs = []
runs.append(run_col)
runs.append(list(run.values()))
utils.save_csv(config["runs_path"], runs)

remarks = []
remarks.append(remark_col)
remarks.append(list(remark_1.values()))
remarks.append(list(remark_2.values()))
utils.save_csv(config["remarks_path"], remarks)

utils.save_json(config["config_path"], config)
