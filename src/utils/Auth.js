import { isEmpty } from 'lodash';
import jwt_decode from "jwt-decode";


const auth = {

    isAuthenticated() {

        const token = localStorage.getItem('token')

        if (!token) {
            return false
        }
        return true
    },

    tokenExp() {

        // const token = auth.get()
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
    },

    remove() {
        localStorage.clear();
    }

}

export default auth;