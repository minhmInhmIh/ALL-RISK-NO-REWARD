import json

with open(r"C:\Code\game\games\game.json", "r") as file:
    game = json.load(file)

class GameState:
    def __init__(self, phase, round, players):
        self.phase = phase
        self.round = round
        self.players = players
    def auction(self, machine_idx, starting_cost):
        machine = game["machines"][machine_idx]["name"]
        print(f"Machine: {machine}")
        print(f"Opening bid: {starting_cost}")

        auction_status = {}

        for player in self.players:
            name = player["name"]
            auction_status[name] = False

        highest_bid = starting_cost
        highest_bidder = None

        passed = 0
        while(len(self.players) - passed > 1):
            for player in self.players:
                if auction_status[player["name"]] == True:
                    continue
                else:
                    if player == highest_bidder:
                        continue
                    current_bid = input(f"{player["name"]}'s bid (say 'pass' if you dont wanna bid) highest bid: {highest_bid}: ")
                    if current_bid == "pass":
                        auction_status[player["name"]] = True
                        passed += 1
                    else:
                        if current_bid != "pass":

                            while((highest_bid - int(current_bid)) % 50 != 0 or int(current_bid) <= highest_bid):
                                current_bid = input(f"{player["name"]}'s bid (say 'pass' if you dont wanna bid) highest bid: {highest_bid}: ")
                                if current_bid == "pass":
                                    auction_status[player["name"]] = True
                                    passed += 1
                                    break
                            if current_bid == "pass":
                                continue
                            else:
                                highest_bid = int(current_bid)
                                highest_bidder = player


            print("--------------------------------------------------------------------")
        if len(self.players) - passed == 1:
            highest_bidder["machines"].append(machine)
            highest_bidder["money"] -= highest_bid
            print(f"SOLD TO {highest_bidder["name"]}.")
            game["machines"][machine_idx]["amount"] -= 1
            game["auction_distribution"][f"round_{self.round}"][game["machines"][machine_idx]["name"]] -= 1
            print(f"{highest_bidder["name"]}'s money left: {highest_bidder["money"]} machines owned: {highest_bidder["machines"]}")
        if len(self.players) == passed:

            print(f"{machine} will be relisted.")