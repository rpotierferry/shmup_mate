import utils
import models
class GamesRepository:
    def __init__(self, path):
        self.path = path
        self.data = utils.load_csv(path)
        self.games = GamesRepository.build_games_list(self.data)
        self.next_id = len(self.games) + 1

    def all(self):
        return self.games

    def find(self, id):
        return self.data[id]

    def create(self, game_info):
        row = []
        row.append(self.next_id)
        row.append(game_info["title"])
        row.append(game_info["developper"])
        row.append(game_info["platform"])
        self.data.append(row)
        self._save()

    def _save(self):
        utils.save_csv(self.path, self.data)

    @classmethod
    def build_games_list(cls, data):
        games = []
        for row in data[1:]:
            games.append(models.Game(
                row[0], row[1], row[2], row[3])
            )
        return games

class RunsRepository:
    def __init__(self):
        pass

class RemarksRepository:
    def __init__(self):
        pass
