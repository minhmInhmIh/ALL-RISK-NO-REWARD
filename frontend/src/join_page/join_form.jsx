import React, { useState } from "react";

function JoinForm(props) {

    const [name, setName] = useState("");

    if (props.maxPlayerReached === false){
        return (
            <form action="" onSubmit={async (event) => {
                event.preventDefault();
                await FetchName(name);
                setName("");
                props.fetchgameinfo();
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
    const URL = "http://localhost:8000/join";
    return fetch(URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    })
}
    

export default JoinForm;