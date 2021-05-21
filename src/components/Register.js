import React from 'react'
import axios from 'axios'
import { Redirect } from 'react-router-dom';

import Auth from '../utils/Auth.js'

function Register() {

    if (Auth.isAuthenticated() && Auth.verifiedEmail()) {
        console.log(Auth.verifiedEmail())
        return(<Redirect to="/stories" />)
    }

    const token = Auth.get()
    let myConfig = {
        headers: {
            "Authorization": token,
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
     }

    const setEmail = () => {
        axios.post('http://127.0.0.1:5000/email', {email:"test@email.com"} , myConfig)
        .then(res => {
            console.log(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }

    return (
        <div className="register-page">
            <p className="register-text">We need a way to send you your photos! At the
                end of the month we will email you a detailed
                image of your monthly Spotify listening habits.
                If you decide to cancel this service at any time
                we will delete your account and email.
            </p>
            <input
                    type="text"
                    placeholder="Email"
                    name="email"
                />
                <button onClick={setEmail}>Submit Email</button>
        </div>
    )
}

export default Register

// {/* {errors?.email && <ErrorMessage message={errors.email.message} />} */}

// this is what is breaking the entire form
// {...register("email", {
//     required: "Email is required.", 
//     pattern: {
//         value: /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/,
//         message: "Please enter a valid email"
//     }
//     }
// )}