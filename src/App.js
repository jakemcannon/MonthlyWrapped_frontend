import React from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './components/LandingPage.js';

import Nav from './components/Nav.js'
import Footer from './components/Footer.js'
import LandingPage from './components/LandingPage.js';
import Stories from './components/Stories.js'
import Account from './components/Account.js'
import About from './components/About.js'
import Cred from './components/Cred.js'
import PrivateRoute from './components/PrivateRoute.js'

function App() {

  // useEffect(() => {
  //   fetch('/home').then(response => 
  //     response.json().then(data => {
  //       console.log(data);
  //   }))
  // }, [])

  return (
    <Router>
      <Nav />
        <Switch>
        <Route path="/" exact component={LandingPage}/>
          <PrivateRoute path="/stories" component={Stories}/>
          <Route path="/account" component={Account}/>
          <Route path="/about" component={About}/>
          <Route path="/cred" component={Cred}/>
        </Switch>
      <Footer />
    </Router>
  );
}

export default App;


// return (
//   <div className="App">
//     <img src={logo} className="App-photo" alt="logo" />
//     <HomePage />
//      <h2>
//        Create monthly Instagram stories based on your Spotify listening trends
//      </h2>
//      <p>
//        Once a month we will email or text you your official Spotify listening trends for the month
//      </p>
//  </div>
// );
// }