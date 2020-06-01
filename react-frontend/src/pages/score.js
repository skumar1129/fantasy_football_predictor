import React from 'react';
import ScoreComp from '../components/score';
import scorepage from '../assets/scorepage.jpg'

const Score = () => {
    return(
        <div className="scoring-page">
            <div className="jumbotron">
                <h3 className='display-4'>2020 Fantasy Projections</h3>
                <ScoreComp/>
                <img className="img-fluid mb-2" src={scorepage} alt='' />
            </div> 
        </div>
    )
}

export default Score;