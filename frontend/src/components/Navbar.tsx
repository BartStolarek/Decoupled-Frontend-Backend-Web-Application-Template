// components/Navbar.tsx
import React, { useState, useEffect } from 'react';
import styles from '../styles/Navbar.module.css'; // Importing CSS module
import Link from 'next/link'; // Using Next.js Link for navigation without page refresh
import { useAuth } from '@/contexts/AuthContext';
import useCheckRole from '@/hooks/useCheckRole';


const Navbar = () => {
	const [menuOpen, setMenuOpen] = useState(false);
	const { user, isAuthenticated, logout } = useAuth();
	const { isLoading, userRole } = useCheckRole();

	const handleProfile = () => {
		window.location.assign(`/profile/${user?.user_id}`)
	};

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

	const handleAdmin = async () => {
		const isAdmin = await isAuthenticated('Administrator');
		if (!isAdmin) {
			alert('You are not authorized to access this page');
			return;
		}
		window.location.assign('/admin')
	}

	return (
		<>
			<nav className="navbar bg-neutral z-10 min-w-full shadow-lg ">
				{/* Navbar Start */}
				<div className="navbar-start">
					<div
						tabIndex={0}
						className="menu-icon btn btn-ghost btn-small h-6 w-8 mx-3 p-0 min-h-0 z-30 sm:hidden"
						role="button"
						onClick={() => setMenuOpen(!menuOpen)}
					>
						<span className={`${styles.bar} ${menuOpen ? styles.activeBar1 : ''}`}></span>
						<span className={`${styles.bar} ${menuOpen ? styles.activeBar2 : ''}`}></span>
						<span className={`${styles.bar} ${menuOpen ? styles.activeBar3 : ''}`}></span>
					</div>
					<div className="hidden sm:flex gap-4 mx-16">
						<Link href="/products" className="btn btn-ghost hover:text-secondary">
							Products
						</Link>
						<Link href="/services" className="btn btn-ghost hover:text-secondary">
							Services
						</Link>
					</div>
				</div>

				{/* Navbar Center */}
				<div className="navbar-center">
					<Link href="/">
						<img src="/images/logo/logo-navbar.png" alt="Logo" />
					</Link>
				</div>

				{/* Navbar End */}
				<div className="navbar-end sm:pr-4" id="navbarEnd">
					{!isLoading && user ? (
						<div className="dropdown dropdown-end">
							<div className="dropdown dropdown-end">
								<div tabIndex={0} role="button" className="btn btn-ghost btn-sm avatar">
									<div className="w-10 rounded-full shadow">
										<img alt="Tailwind CSS Navbar component" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
									</div>
								</div>
								<ul tabIndex={0} className="mt-3 z-999 p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
									<li><button onClick={handleProfile}>Profile</button></li>
									{userRole === 'Administrator' && (
										<li>
											<button onClick={handleAdmin}>
												Admin
												<span className="badge">New</span>
											</button>
										</li>
									)}
									<li><button onClick={handleLogout}>Logout</button></li>
								</ul>
							</div>
						</div>
					) : (
						<div className="flex gap-8">
							<button onClick={handleRegister} className="btn btn-ghost btn-sm w-24 hidden md:block text-accent font-bold  hover:text-secondary">Register</button>
							<button onClick={handleLogin} className="btn border-secondary bg-gradient-to-r from-primary to-secondary btn-sm shadow w-24 hidden md:block text-text font-bold text-white">Login</button>
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
						<a href="/" className="text-4xl font-bold">Logo</a>
					</div>
					<div className="space-y-16">
						<a href="/" className="block text-5xl mb-4">Home</a>
						<a href="/products" className="block text-5xl">Products</a>
						<a href="/services" className="block text-5xl">Services</a>
						<a href="/about" className="block text-5xl">About</a>
						<a href="/contact" className="block text-5xl">Contact Us</a>
					</div>
				</div>
			</div>
		</>
	);
};

export default Navbar;
