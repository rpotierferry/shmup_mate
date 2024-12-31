def main_menu():
    print("1. See game list")
    print("2. Add a game")
    print("x. quit")

    choice = input("What next?")
    return choice

def show_game(game):
    print(game.title)

def ask_thing(thing):
    choice = input(f"{thing}?")
    return choice
