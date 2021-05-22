import React, {useState} from 'react'
import axios from 'axios'
import { Redirect } from 'react-router-dom';

import Auth from '../utils/Auth.js'

function Register() {

    const [redirect, setRedirect] = useState("");

    if (Auth.isAuthenticated() && Auth.verifiedEmail()) {
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
        // todo, update with form data
        axios.post('http://127.0.0.1:5000/email', {email:'test@gmail.com'} , myConfig)
        .then(res => {
            Auth.set(res.data)
            setRedirect('/stories')
        })
        .catch(err => {
            console.log(err)
        })
    }

    if (redirect) {
        return <Redirect to="{redirect}" />
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