class Game:
    def __init__(self, game_info):
        self.id = int(game_info["id"])
        self.title = game_info["title"]
        self.dev = game_info["dev"]
        self.platform = game_info["platform"]
        self.runs = []

class Run:
    def __init__(self, run_info):
        self.id = int(run_info["id"])
        self.game_id = int(run_info["game_id"])
        self.state = run_info["state"]
        self.score = int(run_info["score"])
        self.stage = (run_info["stage"])
        self.remarks = []

class Remark:
    def __init__(self, rem_info):
        self.id = int(rem_info["id"])
        self.run_id = int(rem_info["run_id"])
        self.text = rem_info["text"]

class Stages:
    def __init__(self):
        pass

class Strategies:
    def __init__(self):
        pass
