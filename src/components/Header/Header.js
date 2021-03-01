import React from 'react'

function Header() {
    return (
        <div>
            {/* <section>
            Login
            </section>
            <section>Sign Up</section> */}
            <a href="/Login" className="">Log in</a>
            <a href="/register" className="">Sign Up</a>
            <a href="/account" className="">Account</a>
        </div>
    )
}

export default Header
