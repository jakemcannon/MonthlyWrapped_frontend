import React from 'react'
import { Link } from 'react-router-dom';
import logo from '../logo.svg'

function Nav() {
    return (
        <nav>
            <ul className="nav-links">
            <img className="nav-img" src={logo} alt='logo'/>
                <Link className="nav-link" to='/about'>
                    <li>About</li>
                </Link>
                <Link className="nav-link" to="/content">
                    <li>Content</li>
                </Link>
            </ul>
        </nav>
    )
}

export default Nav
