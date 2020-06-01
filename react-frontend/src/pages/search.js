import React from 'react';
import searchpage from '../assets/searchpage.jpg';
import SearchComp from '../components/search';
import { Link } from 'react-router-dom';





const Search = () => {
    const grabPlayer = () => {

    }
    return(
        <div className='search-page'>
            <div className='jumbotron'>
                <form>
                    <h1 className="display-4 mb-2">Choose your player</h1>
                    <SearchComp/>
                    <Link className="btn btn-primary" to='/score' onClick={grabPlayer}>Submit</Link>
                </form>
                <img className='img-fluid mt-2' src={searchpage} alt='' />
            </div>
        </div>
    )
}

export default Search;