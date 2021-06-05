import React from 'react'

import song_image from '../example_songs.png'
import artist_image from '../example_artists.png'

function MonthlyImage() {
    return (
        <div>
            <h1>This is the test image generation endpoint</h1>
         <img className="photo-list-image" src={song_image} className="App-photo" alt="" />
         <img className="photo-list-image" src={artist_image} className="App-photo" alt="" />
         </div>
    )
}

export default MonthlyImage
