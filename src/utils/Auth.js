import { isEmpty } from 'lodash';


const auth = {

    isAuthenticated() {

        const token = localStorage.getItem('token')

        if (!token) {
            console.log("Token does not exist")
            return false
        }
        return true
    },

    verifiedEmail() {
        return true
    },
    
    tokenExp() {

        const token = auth.get()
        // let decodedToken = jwt.decode(token, {complete: true})
        

    },

    set(value) {
        if (isEmpty(value)) {
            return null;
          }

        return localStorage.setItem('token', 'Bearer ' + value)
    },

    get() {
        const token = localStorage.getItem('token')
        return token
    }

}

export default auth;