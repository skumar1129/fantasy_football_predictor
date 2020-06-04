import React, { useState, useContext } from 'react';
import searchpage from '../assets/searchpage.jpg';
import SearchComp from '../components/search';
import { Link } from 'react-router-dom';
import { grabPlayer } from '../api/api_service';
import { PlayerContext } from '../context/playerContext';





const Search = () => {
    const [name, setName] = useState('');
    const { editPlayer } = useContext(PlayerContext);
    
    const grabName = (plauyerName) => {
        setName(plauyerName);
    }
    const getPlayer = () => {
        grabPlayer(name)
        .then(res => res.data)
        .then(data => {
            editPlayer(data);
        })
        .catch(err => console.log(err));
    }
    return(
        <div className='search-page'>
            <div className='jumbotron'>
                <form>
                    <h1 className="display-4 mb-2">Choose your player</h1>
                    <SearchComp sendName={grabName} />
                    <Link className="btn btn-primary" to='/score' onClick={getPlayer}>Submit</Link>
                </form>
                <img className='img-fluid mt-2' src={searchpage} alt='' />
            </div>
        </div>
       
    )
}

export default Search;