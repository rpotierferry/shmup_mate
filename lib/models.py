class Game:
    def __init__(self, id, title, dev, platform):
        self.id = id
        self.title = title
        self.dev = dev
        self.platform = platform

class Run:
    def __init__(self, id, game_id, state):
        self.id = id
        self.game_id = game_id
        self.state = state

class Remark:
    def __init__(self):
        pass
