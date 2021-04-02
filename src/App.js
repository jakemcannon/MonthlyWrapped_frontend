import React, {useEffect} from 'react';
import './App.css';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import song_image from './example_songs.png'
import artist_image from './example_artists.png'
import Header from './components/Header/Header.js';

function App() {

  useEffect(() => {
    fetch('/home').then(response => 
      response.json().then(data => {
        console.log(data);
    }))
  }, [])

  return (
    <div className="container">
      {/* <Header /> */}
      <h2>Create monthly Instagram stories based on your Spotify listening trends </h2>
      <p className="sub-heading"> Once a month we will email or text you your official Spotify listening trends for the month </p>
      <ul className="photo-list">
        <li>
        <img src={song_image} className="App-photo" />
        </li>
        <li>
        <img src={artist_image} className="App-photo" />
        </li>
      </ul>
      <Button variant="success" onClick={async () => {
        const r = await fetch("/login", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
          }
        }).then(r => 
          r.json().then(d => {
            window.location = d.data
            console.log(d.data);
        }))
      }}
      >
        Login
      </Button>
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