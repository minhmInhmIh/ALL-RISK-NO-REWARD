import JoinForm from "./join_form.jsx";
import PLayerList from "./playerList.jsx";
import Countdown from "./countdown.jsx";
import React, { useState , useEffect} from "react";

function Join() {
  const [maxPlayers, setMaxPlayers] = useState(0);
  const [playersName, setPlayersName] = useState([]);
  const [countdown, setCountdown] = useState(0)
  const [maxPlayerReached, setMaxPlayerReached] = useState(false)
  useEffect(() => {
      console.log("opening websocket")
      const socket = new WebSocket("ws://localhost:8000/ws");

      socket.onmessage = (event) => {
          const data = JSON.parse(event.data);

          if (data.type === "countdown") {
              setCountdown(data.value);
          }
          else if (data.type === "max_player_reached"){
            setMaxPlayerReached(data.value)
          }
      };

      return () => {
          socket.close();
      };
  }, []);
  function fetchgameinfo() {
      const URL = "http://localhost:8000/game-info";
      fetch(URL)
          .then(response => response.json())
          .then(data => {
              setMaxPlayers(data.max_players);
              setPlayersName(data.players_names);
          })
          .catch(error => console.error("Error fetching game info:", error));
  }
  return (
    <div>
      <h1>Welcome to ALL RISK NO REWARD</h1>
      <JoinForm fetchgameinfo={fetchgameinfo} maxPlayerReached = {maxPlayerReached}/>
      <PLayerList players_names={playersName} number_of_players_joined={playersName.length} max_players={maxPlayers} />
      <Countdown countdown = {countdown} maxPlayerReached = {maxPlayerReached}/>
    </div>

  );
}

export default Join;