import React, {useState, useEffect } from 'react'
import Button from 'react-bootstrap/Button';
const s_images = [
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

const a_images = [
    {id:1, imageName: 'january.png'},
    {id:2, imageName: 'february.png'},
    {id:3, imageName: 'march.png'},
    {id:4, imageName: 'april.png'},
    {id:5, imageName: 'may.png'},
    {id:6, imageName: 'june.png'},
    {id:7, imageName: 'july.png'},
    {id:8, imageName: 'august.png'},
    {id:9, imageName: 'september.png'},
    {id:10, imageName: 'october.png'},
    {id:11, imageName: 'november.png'},
    {id:12, imageName: 'december.png'},
]

function Content() {

    const [data, setData] = useState(s_images)

    return (
        <div>
            <div className="menu">
                <h1 className="menu-header">Your stories</h1>
                <Button onClick={() => setData(s_images)}  className="menu-btn" variant="success shadow-none"> Top Songs </Button>
                <Button onClick={() => setData(a_images)} className="menu-btn" variant="success shadow-none"> Top Artists </Button>
            </div>
            <div className="image-grid">
            {data.map(image => 
                <div key={image.id}>
                    <img class="grid-image" src={`./song_images/${image.imageName}`} alt="image"/>
                </div>  
            )}
            </div>
        </div>
    )
}

export default Content