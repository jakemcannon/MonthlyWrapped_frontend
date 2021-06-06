import React, {useState, useEffect} from 'react'
import axios from 'axios'
import Auth from '../utils/Auth.js'
import song_image from '../example_songs.png'
import artist_image from '../example_artists.png'

function MonthlyImage() {
    const [isLoading, setLoading] = useState(true);
    const [currentMonth, setCurrentMonth] = useState([])

    useEffect(() => {
        const token = Auth.get()
        axios.get('http://127.0.0.1:5000/generate_images', {
            headers: {'Authorization': token}
        })
        .then(res => {
            setCurrentMonth(res.data)
            setLoading(false);
        })
        .catch(err => {
            console.log(err)
        })
    }, [])

    return (
        <div>
        <h1>This is the test image generation endpoint</h1>
        <p>It may take about 5 secs to load</p>
         {!isLoading  && 
         <div>
            <img className="photo-list-image" src={currentMonth[0].song} alt=""/>
            <img className="photo-list-image" src={currentMonth[1].artist} alt=""/>
        </div>}
         </div>
    )
}

export default MonthlyImage
