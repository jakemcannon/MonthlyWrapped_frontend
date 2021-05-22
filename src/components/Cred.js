import {Redirect, useLocation} from 'react-router-dom'
import Auth from '../utils/Auth.js'

function Cred() {

    // this is a hook, can't use conditionally
    const url_token = useLocation().search

    // get token from LocalStorage
    if (url_token === "") {
        const bearer_token = Auth.get()
        if (!bearer_token) { // TODO or expired
            return(<Redirect to='/'/>)
        }
    } else {
        const bearer_token = new URLSearchParams(url_token).get('token')
        Auth.set(bearer_token)
    }
    return (<Redirect to='/stories'/>
    )
}

export default Cred
