import React, {useState, useEffect} from 'react'
import axios from 'axios'

function Account() {

    const [account, setAccount] = useState({})

    let myConfig = {
        headers: {
           Authorization: "Bearer "
        }
     }

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/user', myConfig)
        .then(res => {
            console.log(res.data)
            setAccount(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }, [])

    return (
        <div>
            <h1>Account Page</h1>
            <div>{account.id}</div>
            <div>{account.user_id}</div>
        </div>
    )
}

export default Account
