import repositories
import views

""" handles the data related to games """
class GamesController:
    def __init__(self, path_games, path_runs):
        self.path_games = path_games
        self.path_runs = path_runs


    """ find a specific game """
    def find(self, gid:int):
        games_repo = self.load_games_repo()
        game = games_repo.get_game(gid)
        # needs to load an up-to-data run list
        runs_repo = self.load_runs_repo()
        game.runs = runs_repo.get_game_runs(game)
        return game

    """ add a new game """
    def add(self):
        games_repo = self.load_games_repo()
        title = views.ask_thing("Title")
        dev = views.ask_thing("Developper")
        platform = views.ask_thing("Platform")
        games_repo.create({
            "title" : title,
            "developper" : dev,
            "platform" : platform
        })

    """ list all games """
    def index(self):
        games_repo = self.load_games_repo()
        games = games_repo.all()
        views.clear()
        for game in games:
            views.show_game(game)

    def load_games_repo(self):
        return repositories.GamesRepository(self.path_games)

    def load_runs_repo(self):
        return repositories.RunsRepository(self.path_runs)

""" handles the data related to runs """
class RunsController:
    def __init__(self, path_runs, path_remarks):
        self.path_runs = path_runs
        self.path_remarks = path_remarks


    def find_game_run(self, run_id:int, game):
        run = game.runs[int(run_id) - 1]
        rem_repo = self.load_remarks_repo()
        run.remarks = rem_repo.get_run_remarks(run)
        return run

    def add(self, game):
        state = views.ask_thing("State")
        stage = views.ask_thing("Stage")
        score = views.ask_thing("Score")
        runs_repo = self.load_runs_repo()
        runs_repo.create({
            "game_id" : game.id,
            "state" : state,
            "stage" : stage,
            "score" : score
        })

    def load_runs_repo(self):
        return repositories.RunsRepository(self.path_runs)

    def load_remarks_repo(self):
        return repositories.RemarksRepository(self.path_remarks)

class RemarksController:

    def __init__(self, path_remarks):
        self.path_remarks = path_remarks

    def add(self, run):
        text = views.ask_thing("Remark")
        rem_repo = self.load_remarks_repo()
        rem_repo.create({
            "text" : text,
            "run_id" : run.id
        })

    def load_remarks_repo(self):
        return repositories.RemarksRepository(self.path_remarks)
