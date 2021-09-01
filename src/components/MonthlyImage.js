import React, {useState, useEffect} from 'react'
import axios from 'axios'
import Auth from '../utils/Auth.js'
import song_image from '../example_songs.png'
import artist_image from '../example_artists.png'
import { css } from "@emotion/react";
import BeatLoader from "react-spinners/BeatLoader";

const override = css`
  display: block;
  margin: 100 auto;
  border-color: red;
`;

function MonthlyImage() {
    const [isLoading, setLoading] = useState(true);
    const [currentMonth, setCurrentMonth] = useState([])

    useEffect(() => {
        const token = Auth.get()
        axios.get('http://127.0.0.1:5000/generate_images_test', {
            headers: {'Authorization': token}
        })
        .then(res => {
            // I think we need some logic here to determine if we got image urls back or general 200 response as a background job
            // SEE COMMENT IN PYHTON CODE
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

    // If !last_day_of_month -> No api request, just display text message
    //      I belive the solution is to conditionally render component
    // IF last_day_of_month -> api request
    //          Backend: (image has already been generated) -> query from s3
    //          Backend: (not already generated) -> to the lambda workflow

    return (
        <div>
        <div className="heading">
            <BeatLoader className="spinner" color={"#76CE53"} loading={isLoading} css={override} size={20} margin={15} />  
        </div>
         {!isLoading  && 
         <div>
            <h1 className="heading">Here are your June 2021 stories</h1>    
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
