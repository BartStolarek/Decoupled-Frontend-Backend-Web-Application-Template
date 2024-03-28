// components/Navbar.tsx
import React, { useState, useEffect } from 'react';
import styles from '../styles/Navbar.module.css'; // Importing CSS module

const Navbar = () => {
	const [menuOpen, setMenuOpen] = useState(false);
	const [token, setToken] = useState('');

	useEffect(() => {
		// Simulating retrieval of token from localStorage
		setToken(localStorage.getItem('jwtToken') || '');
	}, []);

	return (
		<>
			<nav className="navbar bg-neutral z-10 min-w-full shadow-lg">
				<div className="navbar-start">
					<div
						tabIndex={0}
						className="menu-icon btn btn-ghost btn-small h-6 w-8 mx-3 p-0 min-h-0 z-30 fixed"
						role="button"
						onClick={() => setMenuOpen(!menuOpen)}
					>
						<span className={`${styles.bar} ${menuOpen ? styles.activeBar1 : ''}`}></span>
						<span className={`${styles.bar} ${menuOpen ? styles.activeBar2 : ''}`}></span>
						<span className={`${styles.bar} ${menuOpen ? styles.activeBar3 : ''}`}></span>
					</div>
				</div>
				<div className="navbar-center">
					<a href="/" className="btn btn-ghost text-3xl text-text">Logo</a>
				</div>
				<div className="navbar-end" id="navbarEnd">
					{token ? (
						<div className="dropdown dropdown-end">
							{/* User Avatar and Dropdown */}
						</div>
					) : (
						<div className="flex gap-8">
							<a href="/register" className="btn btn-ghost btn-sm w-24 hidden md:block text-lg text-text ">Register</a>
							<a href="/login" className="btn btn-secondary btn-sm shadow w-24 hidden md:block text-text text-lg">Login</a>
						</div>
					)}
				</div>
			</nav>

			<div id="menuOverlay" className={`fixed inset-0 transform ${menuOpen ? 'translate-x-0' : '-translate-x-full'} bg-black bg-opacity-90 backdrop-blur-sm z-20 min-w-full items-top text-white container transition-transform duration-300 ease-in-out`}>
				<div className="flex flex-col min-w-full space-y-20">
					<div className="text-right min-w-full">
						<a href="#" className="text-4xl font-bold">Logo</a>
					</div>
					<div className="space-y-16">
						<a href="/" className="block text-5xl mb-4">Home</a>
						<a href="/about" className="block text-5xl">About</a>
					</div>
				</div>
			</div>
		</>
	);
};

export default Navbar;
