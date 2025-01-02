import os

def splash():
    clear()
    print("--- Welcome to Shmup Mate ---")

def main_menu():
    print("1. See game list")
    print("x. quit")

    return input("What next?")

def show_game(game):
    print(f"{game.id} - {game.title}")

def show_runs(runs):
    print("--------------\n")
    i = 0
    for run in runs:
        i +=1
        print(f"{i} - {run.score} - {run.state}")

def show_game_info(game):
    print(f"Game: {game.title}")
    print(f"Developper: {game.dev}")
    print(f"Platform: {game.platform}")

def choose_game():
    return input("Choose game (x to go back)")

def ask_thing(thing):
    choice = input(f"{thing}?")
    return choice

def game_management_menu():
    return input("View which run? ('a' to add a new run, 'x' to go back)")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_run(run):
    print(f"{run.score} - {run.state}")
    for remark in run.remarks:
        print(remark.text)
    return input("'x' to go back")
