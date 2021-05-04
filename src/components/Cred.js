import {Redirect, useLocation} from 'react-router-dom'
import Auth from '../utils/Auth.js'

function Cred() {

    // this is a hook, can't use conditionally
    const search = useLocation().search

    console.log(search)
    console.log("^ searchhhhhh")
    if (search === "") {
        const token = Auth.get()
        if (!token) {
            return(<Redirect to='/'/>)
        }
    } else {
        const token = new URLSearchParams(search).get('token')
        Auth.set(token)
    }
    return (<Redirect to='/stories'/>
    )
}

export default Cred
