import React, {useEffect} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './components/LandingPage.js';
import LandingPage from './components/LandingPage.js';

function App() {

  // useEffect(() => {
  //   fetch('/home').then(response => 
  //     response.json().then(data => {
  //       console.log(data);
  //   }))
  // }, [])

  return (
    <div className="container">
      <LandingPage />
    </div>
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