import controllers
import views

class Router:
    def __init__(self, params):
        self.running = True
        self.g_controller = controllers.GamesController(
            params["games_path"],
            params["runs_path"]
            )
        self.r_controller = controllers.RunsController(
            params["runs_path"],
            params["remarks_path"]
        )
        self.current_game = False
        views.splash()

    def run(self):
        while self.running:
            choice = views.main_menu()
            match choice:
                # see games list
                case "1":
                    self.g_controller.index()
                    self.select_game()
                # add a new game
                case "2":
                    self.g_controller.add()
                # quit the app
                case"x":
                    views.clear()
                    self.running = False

    # game selection menu
    def select_game(self):
        choice = views.choose_game()
        # return to main menu
        if choice == "x":
            views.clear()
            self.run()
        # go to specific game view
        else:
            self.game_choice = choice
            self.load_game()
            self.manage_game()

    def manage_game(self):
        views.clear()
        views.show_game_info(self.current_game)
        views.show_runs(self.current_game.runs)

        choice = views.game_management_menu()
        if choice == "x":
            self.run()
        elif choice == "a":
            views.clear()
            self.r_controller.add(self.current_game)
            self.load_game()
            self.manage_game()
        else:
            run = self.r_controller.find_game_run(choice, self.current_game)
            self.manage_run(run)

    def manage_run(self, run):
        views.clear()
        views.show_run(run)
        self.manage_game()

    def load_game(self):
        self.current_game = self.g_controller.find(self.game_choice)
