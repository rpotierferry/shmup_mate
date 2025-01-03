import controllers
import views

class Router:
    def __init__(self, params):
        self.running = True
        self.g_controller = controllers.GamesController(
            params["games_path"],
            params["runs_path"]
            )
        self.run_controller = controllers.RunsController(
            params["runs_path"],
            params["remarks_path"]
        )
        views.splash()

    def run(self):
        while self.running:
            choice = views.main_menu()
            match choice:
                # quit the app
                case"x":
                    views.clear()
                    self.running = False
                # see games list
                case "1":
                    self.select_game()
                # add a new game
                case "2":
                    self.g_controller.add()

    # game selection menu
    def select_game(self):
        views.clear()
        self.g_controller.index()
        choice = views.choose_game()
        # return to main menu
        if choice == "x":
            views.clear()
            self.run()
            return
        # add a game
        if choice == "a":
            self.g_controller.add()
            self.select_game()
            return
        # go to specific game view
        else:
            self.load_game(choice)
            self.manage_game()
            return

    def manage_game(self):
        views.clear()
        views.show_game_info(self.current_game)
        views.show_runs(self.current_game.runs)

        choice = views.game_management_menu()
        if choice == "x":
            self.select_game()
            self.unload_game()
            return
        elif choice == "a":
            views.clear()
            self.run_controller.add(self.current_game)
            self.load_game(self.current_game.id)
            self.manage_game()
            return
        else:
            run = self.run_controller.find_game_run(choice, self.current_game)
            self.manage_run(run)
            return

    def manage_run(self, run):
        views.clear()
        views.show_run(run)
        self.manage_game()
        return

    def load_game(self, gid):
        self.current_game = self.g_controller.find(gid)

    def unload_game(self):
        self.current_game = None
