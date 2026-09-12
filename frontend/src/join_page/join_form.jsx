import React, { useState } from "react";
const ip_address = import.meta.env.VITE_IP_ADDRESS;
console.log(ip_address)
function JoinForm(props) {
    const [name, setName] = useState("");

    if (props.maxPlayerReached === false){
        return (
            <form action="" onSubmit={async (event) => {
                event.preventDefault();
                const response = await FetchName(name);
                if(response.ok)
                {
                    const data = await response.json()
                    props.setPlayerId(data.player_id)
                    sessionStorage.setItem("player_id", data.player_id)
                    setName("");
                    props.fetchgameinfo();
                }
                else{
                    console.warn(`'${name}' already exists`);
                }
            }}>
                <div className="input-box">
                    <input value={name} onChange={(event) => setName(event.target.value)} type="text" placeholder="Enter your name" />
                </div>
                <div>
                    <button type="submit">Join Game</button>
                </div>
            </form>
        )
    }



}

function FetchName(name) {
    const URL = `http://${ip_address}:8000/join`    
    return fetch(URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    })
}
    

export default JoinForm;