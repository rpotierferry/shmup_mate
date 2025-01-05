import controllers
import views

class Router:
    def __init__(self, params):
        self.running = True
        self.games_path = params["games_path"]
        self.runs_path = params["runs_path"]
        self.remarks_path = params["remarks_path"]
        self.g_controller = controllers.GamesController(
            self.games_path,
            self.runs_path
            )
        self.runs_controller = controllers.RunsController(
            self.runs_path,
            self.remarks_path
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
                    self.g_controller.load_games_repo()
                    return

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
            self.g_controller.load_games_repo()
            self.select_game()
            return
        # go to specific game view
        else:
            self.load_game(int(choice))
            self.manage_game()
            return

    def manage_game(self):
        # displays game info and runs
        views.clear()
        views.show_game_info(self.current_game)
        views.show_runs(self.current_game.runs)

        choice = views.game_management_menu()
        # go back
        if choice == "x":
            self.select_game()
            self.unload_game()
            return
        # add a new run
        elif choice == "a":
            views.clear()
            self.runs_controller.add(self.current_game)
            self.runs_controller.load_runs_repo()
            self.load_game(self.current_game.id)
            self.manage_game()
            return
        else:
            run = self.runs_controller.find_game_run(int(choice), self.current_game)
            self.manage_run(run)
            return

    def manage_run(self, run):
        views.clear()
        choice = views.show_run(run)
        if choice == "x":
            self.manage_game()
            return
        else:
            r_controller = controllers.RemarksController(self.remarks_path)
            r_controller.add(run)
            self.load_game(self.current_game.id)
            run = self.runs_controller.find_game_run(run.id, self.current_game)
            self.manage_run(run)
            return

    def load_game(self, gid:int):
        self.current_game = self.g_controller.find(gid)

    def unload_game(self):
        self.current_game = None
