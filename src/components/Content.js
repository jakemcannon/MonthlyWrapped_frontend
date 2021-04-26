import React, {useState, useEffect } from 'react'
import Button from 'react-bootstrap/Button';
import ImageGrid from './ImageGrid'
import axios from 'axios'

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


const s_img = {
    "2021": [
        {id:1, imageName: 'december.png'},
        {id:2, imageName: 'november.png'},
        {id:3, imageName: 'october.png'},
        {id:4, imageName: 'september.png'},
        {id:5, imageName: 'august.png'},
        {id:6, imageName: 'july.png'},
        {id:7, imageName: 'june.png'},
        {id:8, imageName: 'may.png'},
        {id:9, imageName: 'april.png'},
        {id:10, imageName: 'march.png'},
        {id:11, imageName: 'february.png'},
        {id:12, imageName: 'january.png'},
    ],
    "2020": [
        {id:1, imageName: 'january.png'},
    ],
    "2019": [
        {id:1, imageName: 'january.png'},
    ]
}

const s = [
    {id:1, imageName: 'december.png'},
    {id:2, imageName: 'november.png'},
    {id:3, imageName: 'october.png'},
    {id:4, imageName: 'september.png'},
    {id:5, imageName: 'august.png'},
    {id:6, imageName: 'july.png'},
    {id:7, imageName: 'june.png'},
    {id:8, imageName: 'may.png'},
    {id:9, imageName: 'april.png'},
    {id:10, imageName: 'march.png'},
    {id:11, imageName: 'february.png'},
    {id:12, imageName: 'january.png'},
]

function Content() {

    const [songs, setSongs] = useState([])
    const [artists, setArtists] = useState([])
    const [data, setData] = useState(songs)

    useEffect(() => {

        axios.get('http://127.0.0.1:5000/songs')
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

        axios.get('http://127.0.0.1:5000/artists')
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
                    <div>
                        <ImageGrid year={item.year} images={item.months} />
                    </div>
                )
            }
            </div>
        </div>
    )
}

export default Content