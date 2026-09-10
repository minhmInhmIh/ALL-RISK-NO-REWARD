import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import WebSocket, WebSocketDisconnect
from fastapi import HTTPException
import asyncio
import json
import game_state as game_state
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
GAME_PATH = BASE_DIR / "games" / "game.json"

with open(GAME_PATH, "r") as file:
    game = json.load(file)

app = FastAPI()

ip_address = os.getenv("IP_ADDRESS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",f"http://{ip_address}:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Player(BaseModel):
    name: str

connections = []

async def broadcast(data):
    for connection in connections:
        await connection.send_json(data)

async def start_countdown(t: int):
    if len(game_state.players_name) >= game["number_of_players"]:
        game_state.maxed_players_reached = True
        await broadcast({
            "type" : "max_player_reached",
            "value" : True
        })
        while t > 0:
            await broadcast({
                "type" : "countdown",
                "value" : t
            })

            await asyncio.sleep(1)
            t -= 1

        game_state.countdown_finished = True

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    print("WebSocket connected")

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connections.remove(websocket)
        print("WebSocket disconnected")

@app.post("/join")
async def join_game(player: Player):
    player_id = game_state.next_player_id
    if player.name in game_state.players_name:
        raise HTTPException(
            status_code=409,
            detail="Player name already exists"
        )
    game_state.players_name.append(player.name)
    game_state.next_player_id += 1
    print(f"Player {player.name} joined the game. Total players: {len(game_state.players_name)}")
    await broadcast({
        "type" : "players_updated",
        "players" : game_state.players_name
    })
    await start_countdown(5)
    if game_state.countdown_finished:
        game_state.nameToPlayer(player.name)
        return {
            "name" : player.name,
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
    return {
        "name" : player.name,
        "player_id" : player_id
    }
    

@app.get("/game-info")
def get_game_info():
    return {
        "max_players": game["number_of_players"],
        "players_names": game_state.players_name
    }
@app.get("/phase")
def get_phase():
    return {
        "phase": game_state.gameState.phase,
        "round": game_state.gameState.round
    }