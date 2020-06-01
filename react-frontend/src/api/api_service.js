import axios from 'axios';

export const grabNames = () => {
    return axios.get('http://127.0.0.1:5000/names').catch(err => {
        throw new Error(`Name error ${err}`);
    });
}

export const grabPlayer = (player) => {
    return axios.get(`http://127.0.0.1:5000/player/${player}`).catch(err => {
        throw new Error(`Player error ${err}`)
    });
}

