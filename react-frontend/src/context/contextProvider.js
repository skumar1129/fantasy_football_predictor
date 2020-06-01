import React from 'react';
import PlayerContext from './playerContext';

const initalState = {
    name: '',
    fantasyPoints: 0,
    pprPoints: 0,
    draftKingPoints: 0,
    fanDuelPoints: 0
};

<PlayerContext.Provider value={initalState}>
</PlayerContext.Provider>
