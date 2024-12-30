import models

first_game = {
    "id" : 1,
    "title" : "Mushihimesama",
    "developer" : "cave",
    "platform" : "Steam"
}

second_game = {
    "id" : 2,
    "title" : "Dodonpachi",
    "developer" : "Cave",
"platform" : "Mame"
}

test = models.Game(
    first_game["id"],
    first_game["title"],
    first_game["developer"],
    first_game["platform"]
)

print(test)
