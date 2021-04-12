import React from 'react'
import Button from 'react-bootstrap/Button';
import song_image from '../example_songs.png'
import artist_image from '../example_artists.png'
import axios from 'axios'

function LandingPage() {

    const [tempAuth, setTempAuth] = ([])

    let myConfig = {
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
     }

    const tempAuthFunc = () => {
        axios.get('http://127.0.0.1:5000/login', myConfig)
        .then(res => {
            window.location = res.data.data
        })
        .catch(err => {
            console.log(err)
        })
    }

    return (
        <div>
            <h2>Create monthly stories based on your Spotify listening trends </h2>
            <p className="sub-heading"> Once a month we will email or text you your official Spotify listening trends for the month </p>
            <ul className="photo-list">
                <li>
                <img src={song_image} className="App-photo" />
                </li>
                <li>
                <img src={artist_image} className="App-photo" />
                </li>
            </ul>
            <Button variant="success" onClick={tempAuthFunc}> Login </Button>
        </div>
    )
}

export default LandingPage
