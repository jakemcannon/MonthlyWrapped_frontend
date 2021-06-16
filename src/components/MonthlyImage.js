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


    // TODO
    // If not last day of month, have some default message
    // Loading screen

    return (
        <div>
        <h1 className="heading">Here are your July 2021 stories</h1>
        <h1 className="heading">Here are your stories for June 2021</h1>
         {!isLoading  && 
         <div>
             <ul className="photo-list">
                 <li>
                    <img className="photo-list-image" src={currentMonth[0].song} alt=""/>
                 </li>
                 <li>
                    <img className="photo-list-image" src={currentMonth[1].artist} alt=""/>
                 </li>
             </ul>
        </div>}
         </div>
    )
}

export default MonthlyImage
