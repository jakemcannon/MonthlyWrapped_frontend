import React, {useState, useEffect} from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button';
import Auth from '../utils/Auth.js'
import ImageGrid from './ImageGrid'



const s_images = [
    {
        "year": "2021",
        months: [
            {'month':'05.png'}
        ]
    },
    {
        "year": "2020",
        months: [
            {'month':'may.png'},
            {'month':'october.png'},
            {'month':'september.png'}
        ]
    },
    {
        "year": "2019",
        months: [
            {'month':'december.png'},
            {'month':'november.png'},
            {'month':'october.png'},
            {'month':'september.png'},
            {'month':'august.png'},
            {'month':'july.png'},
            {'month':'june.png'},
            {'month':'may.png'},
        ]
    }
]

const a_images = [
    {
        "year": "2021",
        months: [
            {'month':'may.png'}
        ]
    },
    {
        "year": "2020",
        months: [
            {'month':'may.png'},
            {'month':'october.png'},
            {'month':'september.png'}
        ]
    },
    {
        "year": "2019",
        months: [
            {'month':'december.png'},
            {'month':'november.png'},
            {'month':'october.png'},
            {'month':'september.png'},
            {'month':'august.png'},
            {'month':'july.png'},
            {'month':'june.png'},
            {'month':'may.png'},
        ]
    }
]

function Content() {

    const [songs, setSongs] = useState([])
    const [artists, setArtists] = useState([])
    const [data, setData] = useState(songs)

    const token = Auth.get()
    console.log("my token is now coming from Auth service")
    console.log(token)
    useEffect(() => {

        axios.get('http://127.0.0.1:5000/songs', {
            headers: {'Authorization': token}
        })
        .then(res => {
            setSongs(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }, [])

    // the current issue is that the first visit of a renders a blank page for the stories page
    // by adding this we say
    // if the songs variable has changed, also change the data variable
    useEffect(() => {
        setData(songs)
    }, [songs])

    useEffect(() => {

        axios.get('http://127.0.0.1:5000/artists', {
            headers: {'Authorization': token}
        })
        .then(res => {
            setArtists(res.data)
        })
        .catch(err => {
            console.log(err)
        })

    }, [])

    return (
        <div>
            <div className="menu">
                <h1 className="menu-header">Your stories</h1>
                <Button onClick={() => setData(songs)}  className="menu-btn" variant="success shadow-none"> Top Songs </Button>
                <Button onClick={() => setData(artists)} className="menu-btn" variant="success shadow-none"> Top Artists </Button>
            </div>
            <div>
            {
                data.map((item) => 
                    <div key={item.year}>
                        <ImageGrid year={item.year} images={item.months} />
                    </div>
                )
            }
            </div>
        </div>
    )
}

export default Content