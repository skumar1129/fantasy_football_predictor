import React, { useState, useEffect } from 'react';




const ScoreComp = (props) => {
    const [player, setPlayer] = useState('')

    useEffect(() => {
        setPlayer(props.playerInfo);
        console.log(player);
    });

    return(
        <div className='container-fluid'>
            <h5>Player name: {player.name}</h5>
            <h5>Fantasy score: {player.fantasyScores}</h5>
            <h5>PPR score: {player.pprScore}</h5>
            <h5>Draft King score: {player.draftKingScore}</h5>
            <h5>Fan Duel score: {player.fanDuelScore}</h5>
        </div>
    )
}

export default ScoreComp;