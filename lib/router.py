import controllers
import views

class Router:
    def __init__(self, params):
        self.running = True
        self.g_controller = controllers.GamesController(
            params["games_path"],
            params["runs_path"])
        views.splash()

    def run(self):
        while self.running:
            choice = views.main_menu()
            match choice:
                case "1":
                    self.g_controller.index()
                    self.select_game()
                case "2":
                    self.g_controller.add()
                case"x":
                    views.clear()
                    self.running = False

    def select_game(self):
        choice = views.choose_game()
        match choice:
            case "2":
                views.clear()
                self.run()
            case "1":
                choice = views.ask_thing("index")
                self.g_controller.find(choice)
