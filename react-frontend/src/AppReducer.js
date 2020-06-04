export default (state, action) => {
    switch (action.type) {
        case 'Edit_Player':
            const player = action.payload;
            state = {
               name: player.name,
               fantasyScores: player.fantasyScores,
               pprScore: player.pprScore,
               draftKingScore: player.draftKingScore,
               fanDuelScore: player.fanDuelScore
            }
            return state;
        default:
            return state;
    }
};