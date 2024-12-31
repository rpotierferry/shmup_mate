import controllers
import views

class Router:
    def __init__(self):
        self.running = True
        self.g_controller = controllers.GamesController('data/games.csv')
        """ use config file """

    def run(self):
        while self.running:
            choice = views.main_menu()
            match choice:
                case "1":
                    self.g_controller.index()
                case "2":
                    self.g_controller.add()
                case"x":
                    print('bye')
                    self.running = False
