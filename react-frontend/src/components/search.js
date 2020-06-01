import React, { useEffect, useState } from 'react';
import { grabNames } from '../api/api_service';


const SearchComp = () => {
    const [name, setName] = useState([]);
    useEffect(() => {
        grabNames()
        .then(res => res.data)
        .then(data => {
            setName(data.names);
        })
        .catch(err => console.log(err));
    }) 

    return(
        <form>
            <div className="form-group">
                <label className="label mr-1">Players</label>
                <select>
                {name.map((value,index) => {
                    return <option key={index}>{value}</option>
                })}
                </select>
            </div>
        </form>
    )
}

export default SearchComp;