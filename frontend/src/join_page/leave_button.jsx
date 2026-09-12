function LeaveButton(props){
    return(
        <div className="leave_button">
            <button onClick={props.leaveGame}>Leave</button>
        </div>
    )        

}
export default LeaveButton