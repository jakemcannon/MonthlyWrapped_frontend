import React from 'react'
import Button from 'react-bootstrap/Button';

const images = [
    {id:1, imageName: '1.png'},
    {id:2, imageName: '2.png'},
    {id:3, imageName: '3.png'},
    {id:4, imageName: '4.png'},
    {id:5, imageName: '5.png'},
    {id:6, imageName: '6.png'},
    {id:7, imageName: '7.png'},
    {id:8, imageName: '8.png'},
    {id:9, imageName: '9.png'},
    {id:10, imageName: '10.png'},
    {id:11, imageName: '11.png'},
    {id:12, imageName: '12.png'},
]

function Content() {
    return (
        <div>
            <div className="menu">
                <h1 className="menu-header">Your stories</h1>
                <Button className="menu-btn" variant="success shadow-none"> Top Songs </Button>
                <Button className="menu-btn" variant="success shadow-none"> Top Artists </Button>
            </div>
            <div className="image-grid">
            {images.map(image => 
                <div key={image.id}>
                    <img class="grid-image" src={`./song_images/${image.imageName}`} alt="image"/>
                </div>  
            )}
            </div>
        </div>
    )
}

export default Content