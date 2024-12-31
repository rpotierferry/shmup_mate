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
    for run in runs:
        print(f"{run.score} - {run.state}")

def show_game_info(game):
    print(f"Game: {game.title}")
    print(f"Developper: {game.dev}")
    print(f"Platform: {game.platform}")

def choose_game():
    print("1. view a game")
    print("2. go back")

    return input()

def ask_thing(thing):
    choice = input(f"{thing}?")
    return choice

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
