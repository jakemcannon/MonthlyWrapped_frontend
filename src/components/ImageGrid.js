import React from 'react'

const ImageGrid = (props) => (
    <div>
        <h1 className="image-grid-header">{props.year}</h1>
        <div className="image-grid">
            {props.images.map(image => 
                <div>
                    <img class="grid-image" src={`./song_images/${image.month}`} alt="image"/>
                </div>  
            )}
            
        </div>
    </div>
    );

export default ImageGrid
