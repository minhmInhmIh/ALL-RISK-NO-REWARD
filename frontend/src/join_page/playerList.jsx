function PlayerList(props){
    

    return (
        <div>
            <div className="player-list">
                <h2>Players</h2>
                <ul>
                    {props.players_names.map((name, index) => (
                        <li key={index}>{name}</li>
                    ))}
                </ul>
            </div>

            <div className="player_count_indicator">
                <p>{props.number_of_players_joined} / {props.max_players}</p>
            </div>
        </div>
    )
} 

export default PlayerList;