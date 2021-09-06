import { Route, Redirect } from 'react-router-dom';
import Auth from '../utils/Auth.js';

const PrivateRoute = ({component: Component, ...rest}) => {

    // update this to work off local storage

    // additionally, update this to work on token expire

    return (

        // Show the component only when the user is logged in
        // Otherwise, redirect the user to /signin page
        <Route {...rest} render={props => (
            Auth.isAuthenticated() ?
                <Component {...props} />
            : <Redirect to="/" />
        )} />
    );
};

export default PrivateRoute;
