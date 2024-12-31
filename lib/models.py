class Game:
    def __init__(self, id, title, dev, platform):
        self.id = id
        self.title = title
        self.dev = dev
        self.platform = platform
        self.runs = []

class Run:
    def __init__(self, id, game_id, state=False, score=0):
        self.id = id
        self.game_id = game_id
        self.state = state
        self.score = score
        self.remarks = []

class Remark:
    def __init__(self, id, run_id, text):
        self.id = id
        self.run_id = run_id
        self.text = text
