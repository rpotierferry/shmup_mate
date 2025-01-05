import os

def splash():
    clear()
    print("--- Welcome to Shmup Mate ---")

def main_menu():
    print("1. See game list")
    print("2. Add a game")
    print("x. Quit")

    return input("\nWhat next?\n-> ")

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
    return input("\nChoose game (x to go back)\n-> ")

def ask_thing(thing):
    choice = input(f"{thing}?\n-> ")
    return choice

def game_management_menu():
    return input("\nView which run? ('a' to add a new run, 'x' to go back)\n-> ")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_run(run):
    print(f"{run.state} - {run.stage} - {run.score}\n")
    for remark in run.remarks:
        print(f"'{remark.text}'")
    return input("\n'x' to go back, 'a' to add a remark\n-> ")
