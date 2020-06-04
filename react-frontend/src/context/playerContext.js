import React, { createContext, useReducer } from 'react';
import AppReducer from '../AppReducer';

const initialState = {
    name: '',
    fantasyScores: 0,
    pprScore: 0,
    draftKingScore: 0,
    fanDuelScore: 0
}

export const PlayerContext = createContext(initialState);

export const PlayerProvider = ({children}) => {
    const [state, dispatch] = useReducer(AppReducer, initialState);

    function editPlayer(player) {
        // console.log(state);
        dispatch({
            type: 'Edit_Player',
            payload: player
        });
        // console.log(state);
    }

    return (
        <PlayerContext.Provider
        value={{player: state, editPlayer}}>
            {children}
        </PlayerContext.Provider>
    )
}