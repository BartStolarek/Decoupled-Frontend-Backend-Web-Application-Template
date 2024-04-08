// components/Navbar.tsx
import React, { useState, useEffect } from 'react';
import styles from '../styles/Navbar.module.css'; // Importing CSS module
import Link from 'next/link'; // Using Next.js Link for navigation without page refresh
import { useAuth } from '@/contexts/AuthContext';


const Navbar = () => {
	const [menuOpen, setMenuOpen] = useState(false);
	const [user_token, setToken] = useState('');
	const [userRole, setUserRole] = useState('');
	const { user , logout } = useAuth();

	const handleLogout = () => {
		logout();
		window.location.reload(); // Refresh the page
	};

	const handleRegister = () => {
		window.location.assign('/register')
	}

	const handleLogin = () => {
		window.location.assign('/login')
	}
	console.log(user.token);
	console.log(user.role);

	return (
		<>
			<nav className="navbar bg-neutral z-10 min-w-full shadow-lg">

				{/* Navbar Start */}
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

				{/* Navbar Center */}
				<div className="navbar-center">
					<a href="/" className="btn btn-ghost text-3xl text-text">Logo</a>
				</div>

				{/* Navbar End */}
				<div className="navbar-end sm:pr-4" id="navbarEnd">
					{user.token ? (
						<div className="dropdown dropdown-end">
							<div className="dropdown dropdown-end">
								<div tabIndex={0} role="button" className="btn btn-ghost btn-sm avatar">
									<div className="w-10 rounded-full shadow">
										<img alt="Tailwind CSS Navbar component" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
									</div>
								</div>
								<ul tabIndex={0} className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
									<li>
										<a className="justify-between">
											Profile
											<span className="badge">New</span>
										</a>
									</li>
									{user.role === 'Administrator' && (
										<li><a href="/admin/">Admin</a></li>
									)}
									<li><a>Settings</a></li>
									<li><button onClick={handleLogout}>Logout</button></li>
								</ul>
							</div>

						</div>
					) : (
						<div className="flex gap-8">
							<button onClick={handleRegister} className="btn btn-ghost btn-sm w-24 hidden md:block text-lg text-text ">Register</button>
							<button onClick={handleLogin} className="btn btn-secondary btn-sm shadow w-24 hidden md:block text-text text-lg">Login</button>
							<a href="/login" className="btn btn-ghost md:hidden flex justify-center items-center">
								<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" className="w-6 h-6 svg-text">
									<path strokeLinecap="round" strokeLinejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
								</svg>

							</a>
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
						<a href="/contact" className="block text-5xl">Contact Us</a>
					</div>
				</div>
			</div>
		</>
	);
};

export default Navbar;
