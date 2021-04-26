import React from 'react'
import { Link } from 'react-router-dom';
import logo from '../logo.svg'

function Nav() {
    return (
        <nav>
            <ul className="nav-links">
                <Link className="nav-img" to='/'>
                    <li>
                        <img className="nav-img" src={logo} alt='logo'/>
                    </li>
                </Link>
                <Link className="nav-link" to='/about'>
                    <li>About</li>
                </Link>
                <Link className="nav-link" to="/stories">
                    <li>Stories</li>
                </Link>
            </ul>
        </nav>
    )
}

export default Nav
