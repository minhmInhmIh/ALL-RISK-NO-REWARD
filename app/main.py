import game_state as game_state
from engine import GameState, game

def main():
    round_1_auction = game["auction_distribution"]["round_1"]
    round_2_auction = game["auction_distribution"]["round_2"]
     
    leftover = {}
    #round 1 auction   
    current_phase = game["phases"][game_state.current_phase_index]
    if current_phase["type"] == "auction" and current_phase["round"] == 1:
        machines = []
        idx = []
        machine_dict = game["machines"]
        for key, value in round_1_auction.items():
            machines.extend([key] * value)
        for machine in machines:
            for i in range(len(machine_dict)):
                if machine == machine_dict[i]["name"]:
                    idx.append(i)
                    break
        for i in idx:
            game_state.gameState.auction(i, machine_dict[i]["starting_cost"])
        leftover = round_1_auction
        game_state.current_phase_index += 1



    increase = []
    for key, value in leftover.items():
        increase.append(value)
    for i in range(len(increase)):
        round_2_auction[game["machines"][i]["name"]] += increase[i]
    

if __name__ == "__main__":
    main()
