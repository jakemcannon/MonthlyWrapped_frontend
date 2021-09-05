import React, {useState, useEffect} from 'react'
import axios from 'axios'
import Auth from '../utils/Auth.js'
import { css } from "@emotion/react";
import BeatLoader from "react-spinners/BeatLoader";

const override = css`
  display: block;
  margin: 100 auto;
  border-color: red;
`;

function MonthlyImage() {
    const [isLoading, setLoading] = useState(true);
    const [currentMonth, setCurrentMonth] = useState(true);
    const [images, setImages] = useState([])

    useEffect(() => {
        const token = Auth.get()
        axios.get('http://127.0.0.1:5000/current_month', {
            headers: {'Authorization': token}
        })
        .then(res => {
            setImages(res.data)
            if(res.data[0]["curMonth"]) {
                setCurrentMonth(true)
            } else {
                setCurrentMonth(false)
            }
            setImages(res.data)
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
         {!isLoading && currentMonth &&
         <div>
            <h1 className="heading">Here are your June 2021 stories</h1>    
             <ul className="photo-list">
                 <li>
                    <img className="photo-list-image" src={images[1].song} alt=""/>
                 </li>
                 <li>
                    <img className="photo-list-image" src={images[2].artist} alt=""/>
                 </li>
             </ul>
        </div>}
        {!currentMonth &&
            <h1 className="heading">Your stories are still being processed, please check back again soon!</h1>
        }
         </div>
    )
}

export default MonthlyImage
