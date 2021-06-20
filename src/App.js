import React from 'react';
import {BrowserRouter as Router, Switch, Route, Redirect} from 'react-router-dom'

import './index.css';
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
import MonthlyImagePage from './components/MonthlyImagePage'
import MonthlyImage from './components/MonthlyImage'

function App() {
  return (
    <Router>
      <Nav />
        <Switch>
        <Route path="/" exact component={LandingPage}/>
          <PrivateRoute path="/stories" component={Stories}/>
          <PrivateRoute path="/current_month" component={MonthlyImagePage}/>
          <Route path="/account" component={Account}/>
          <Route path="/about" component={About}/>
          <Route path="/cred" component={Cred}/>
        </Switch>
      <Footer />
    </Router>
  );
}

export default App;