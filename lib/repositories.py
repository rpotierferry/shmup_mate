import utils
import models

""" handles storage of games """
class GamesRepository:
    def __init__(self, path):
        self.path = path
        self.data = utils.load_csv(path)
        self.games = self.build_games_list()
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
    def build_games_list(self):
        games = []
        for row in self.data[1:]:
            games.append(models.Game({
                "id" : row[0],
                "title" : row[1],
                "dev" : row[2],
                "platform" : row[3]
                }))
        return games


""" handles storage of runs """
class RunsRepository:
    def __init__(self, path):
        self.path = path
        self.data = utils.load_csv(path)
        self.runs = self.build_runs_list()
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
        row.append(run_info["stage"])
        self.data.append(row)
        self._save()

    """ overwrite the saved data """
    def _save(self):
        utils.save_csv(self.path, self.data)

    def build_runs_list(self):
        runs = []
        for row in self.data[1:]:
            runs.append(models.Run({
                "id" : row[0],
                "game_id" : row[1],
                "state" : row[2],
                "stage" : row[4],
                "score" : row[3]
                }))
        return runs



class RemarksRepository:
    def __init__(self, path):
        self.path = path
        self.data = utils.load_csv(path)
        self.remarks = self.build_remarks_list()

    def get_run_remarks(self, run):
        run_remarks = []
        for remark in self.remarks:
            if remark.run_id == run.id:
                run_remarks.append(remark)
        return run_remarks

    def build_remarks_list(self):
        remarks = []
        for row in self.data[1:]:
            remarks.append(models.Remark({
                "id" : row[0],
                "run_id" : row[1],
                "text" : row[2]})
                )
        return remarks
