import repositories
import views

""" handles the data related to games """
class GamesController:
    def __init__(self, path_games, path_runs):
        self.path_games = path_games
        self.path_runs = path_runs

        self.games_repo = GamesController.load_games_repo(self.path_games)
        self.runs_repo = GamesController.load_runs_repo(self.path_runs)

    """ find a specific game """
    def find(self, id):
        game = self.games_repo.get_game(id)
        game.runs = self.runs_repo.find_runs(game)
        views.show_game_info(game)
        views.show_runs(game.runs)

    """ add a new game """
    def add(self):
        title = views.ask_thing("Title")
        dev = views.ask_thing("Developper")
        platform = views.ask_thing("Platform")
        self.games_repo.create({
            "title" : title,
            "developper" : dev,
            "platform" : platform
        })
        self.games_repo = GamesController.load_games_repo(self.path_games)

    """ list all games """
    def index(self):
        games = self.games_repo.all()
        views.clear()
        for game in games:
            views.show_game(game)

    @classmethod
    def load_games_repo(cls, path):
        return repositories.GamesRepository(path)

    @classmethod
    def load_runs_repo(cls, path):
        return repositories.RunsRepository(path)

""" handles the data related to runs """
class RunsController:
    def __init__(self, path_runs):
        pass
