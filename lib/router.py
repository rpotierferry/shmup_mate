import controllers
import views

class Router:
    def __init__(self, params):
        self.running = True
        self.games_path = params["games_path"]
        self.runs_path = params["runs_path"]
        self.remarks_path = params["remarks_path"]
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
                    g_controller = self.load_games_controller()
                    g_controller.add()
                    self.run()
                    return

    # game selection menu
    def select_game(self):
        views.clear()
        g_controller = self.load_games_controller()
        g_controller.index()
        choice = views.choose_game()
        # return to main menu
        if choice == "x":
            views.clear()
            self.run()
            return
        # add a game
        if choice == "a":
            g_controller.add()
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
            runs_controller = self.load_runs_controller()
            runs_controller.add(self.current_game)
            runs_controller.load_runs_repo()
            self.load_game(self.current_game.id)
            self.manage_game()
            return
        else:
            runs_controller = self.load_runs_controller()
            # this does not find the correct run
            run = self.current_game.runs[int(choice) - 1]
            run = runs_controller.load_run_remarks(run)
            self.manage_run(run)
            return

    def manage_run(self, run):
        views.clear()
        choice = views.show_run(run)
        # goes back
        if choice == "x":
            self.manage_game()
            return
        # add a new remark
        else:
            rem_controller = controllers.RemarksController(self.remarks_path)
            rem_controller.add(run)
            runs_controller = self.load_runs_controller()
            run = runs_controller.load_run_remarks(run)
            self.manage_run(run)
            return

    def load_game(self, gid:int):
        g_controller = self.load_games_controller()
        self.current_game = g_controller.find(gid)

    def unload_game(self):
        self.current_game = None

    def load_games_controller(self):
        return controllers.GamesController(
            self.games_path,
            self.runs_path
            )

    def load_runs_controller(self):
        return controllers.RunsController(
            self.runs_path,
            self.remarks_path
        )
