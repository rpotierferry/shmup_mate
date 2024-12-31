import repositories
import views

class GamesController:
    def __init__(self, path_games):
        self.path_games = path_games
        self.repo = GamesController.load_repo(self.path_games)

    def find(self, id):
        pass

    def add(self):
        title = views.ask_thing("Title")
        dev = views.ask_thing("Developper")
        platform = views.ask_thing("Platform")
        self.repo.create({
            "title" : title,
            "developper" : dev,
            "platform" : platform
        })
        self.repo = GamesController.load_repo(self.path_games)

    def index(self):
        games = self.repo.all()
        for game in games:
            views.show_game(game)

    @classmethod
    def load_repo(cls, path):
        return repositories.GamesRepository(path)
class RunsController:
    def __init__(self, path_runs):
        pass
