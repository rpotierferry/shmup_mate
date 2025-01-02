import utils
import models

""" handles storage of games """
class GamesRepository:
    def __init__(self, path):
        self.path = path
        self.data = utils.load_csv(path)
        self.games = GamesRepository.build_games_list(self.data)
        self.next_id = len(self.games) + 1

    def all(self):
        return self.games

    """ retrieves a game based on its id """
    def get_game(self, id):
        return self.games[int(id) - 1]

    def create(self, game_info):
        row = []
        row.append(self.next_id)
        row.append(game_info["title"])
        row.append(game_info["developper"])
        row.append(game_info["platform"])
        self.data.append(row)
        self._save()

    """ overwrite the saved data """
    def _save(self):
        utils.save_csv(self.path, self.data)

    """ builds an array containing all games """
    @classmethod
    def build_games_list(cls, data):
        games = []
        for row in data[1:]:
            games.append(models.Game(
                row[0], row[1], row[2], row[3])
            )
        return games


""" handles storage of runs """
class RunsRepository:
    def __init__(self, path):
        self.path = path
        self.data = utils.load_csv(path)
        self.runs = RunsRepository.build_runs_list(self.data)
        self.next_id = len(self.runs) + 1

    """ finds all the runs associated with a game """
    def get_game_runs(self, game):
        game_runs = []
        for run in self.runs:
            if run.game_id == game.id:
                game_runs.append(run)
        return game_runs

    def create(self, run_info):
        row = []
        row.append(self.next_id)
        row.append(run_info["game_id"])
        row.append(run_info["state"])
        row.append(run_info["score"])
        self.data.append(row)
        self._save()

    """ overwrite the saved data """
    def _save(self):
        utils.save_csv(self.path, self.data)

    @classmethod
    def build_runs_list(cls, data):
        runs = []
        for row in data[1:]:
            runs.append(models.Run(
                row[0], row[1], row[2], row[3])
                )
        return runs



class RemarksRepository:
    def __init__(self, path):
        self.path = path
        self.data = utils.load_csv(path)
        self.remarks = RemarksRepository.build_remarks_list(self.data)

    def get_run_remarks(self, run):
        run_remarks = []
        for remark in self.remarks:
            if remark.run_id == run.id:
                run_remarks.append(remark)
        return run_remarks

    @classmethod
    def build_remarks_list(cls, data):
        remarks = []
        for row in data[1:]:
            remarks.append(models.Remark(
                row[0], row[1], row[2])
                )
        return remarks
