from engine import GameState, game

players_name = []

players = []

current_phase_index = 0

maxed_players_reached = False
countdown_finished = False

def nameToPlayer(name):
    for name in players_name:
        player = {
            "name" : name,
            "money" : game["starting_money"],
            "machines" : [],
            "resources" : {
                resource: 0
                for resource in game["resources"]
            },
            "products": {
                product: 0
                for product in game["products"]
            }
        }
        players.append(player)

gameState = GameState(game["phases"][current_phase_index]["type"], game["phases"][current_phase_index]["round"], players)

