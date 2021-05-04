import { isEmpty } from 'lodash';


const auth = {

    isAuthenticated() {
        return false
    },

    tokenExp() {

        const token = auth.get()
        // let decodedToken = jwt.decode(token, {complete: true})
        

    },

    set(value) {
        if (isEmpty(value)) {
            return null;
          }

        console.log("hitting my auth service code")
        return localStorage.setItem('token', 'Bearer ' + value)
    },

    get() {
        const token = localStorage.getItem('token')
        console.log("hitting my auth service from get () method the token is...")
        console.log(token)
        return token
    }

}

export default auth;