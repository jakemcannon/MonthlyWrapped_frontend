import React from 'react'
import Button from 'react-bootstrap/Button';
import song_image from '../example_songs.png'
import artist_image from '../example_artists.png'

function LandingPage() {
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
            <Button variant="success" onClick={async () => {
                const r = await fetch("/login", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
                }).then(r => 
                r.json().then(d => {
                    window.location = d.data
                    console.log(d.data);
                }))
            }}
            >
                Login
            </Button>
        </div>
    )
}

export default LandingPage
