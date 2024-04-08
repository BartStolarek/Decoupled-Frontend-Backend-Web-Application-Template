import React, { useState } from 'react';
import Link from 'next/link';
import styles from '../styles/Navbar.module.css';
import useLocalStorage from '@/hooks/useLocalStorage'; // Make sure the path is correct

const Navbar = () => {
	const [menuOpen, setMenuOpen] = useState(false);
	// Adjusted to use useLocalStorage hook
	const [user, setUser] = useLocalStorage('user', { token: '', role: '' });

	const handleLogout = () => {
		setUser({ token: '', role: '' }); // Update using setUser from useLocalStorage
		window.location.reload(); // Refresh the page
	};

	const handleRegister = () => {
		window.location.assign('/register');
	};

	const handleLogin = () => {
		window.location.assign('/login');
	};

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

				<div className="navbar-end sm:pr-4">
					{user?.token ? (
						<div className="dropdown dropdown-end">
							<div tabIndex={0} role="button" className="btn btn-ghost btn-sm avatar">
								<div className="w-10 rounded-full shadow">
									<img alt="User Avatar" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
								</div>
							</div>
							<ul tabIndex={0} className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
								<li><a>Profile<span className="badge">New</span></a></li>
								{user.role === 'Administrator' && <li><a href="/admin/">Admin</a></li>}
								<li><a>Settings</a></li>
								<li><button onClick={handleLogout}>Logout</button></li>
							</ul>
						</div>
					) : (
						<div className="flex gap-8">
							<button onClick={handleRegister} className="btn btn-ghost btn-sm w-24 hidden md:block text-lg text-text">Register</button>
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
				{/* Overlay Content */}
			</div>
		</>
	);
};

export default Navbar;

