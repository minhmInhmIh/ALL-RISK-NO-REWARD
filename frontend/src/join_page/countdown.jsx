function Countdown(props) {
    if(props.maxPlayerReached){
        return(
            <div className="countdown">
                <h2>Game starting in:</h2>
                <p>{props.countdown}</p>
            </div>
        )
    }
}

export default Countdown;