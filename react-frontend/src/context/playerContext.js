import React from 'react';

const PlayerContext = React.createContext({
    name: '',
    fantasyPoints: 0,
    pprPoints: 0,
    draftKingPoints: 0,
    fanDuelPoints: 0
});

export default PlayerContext