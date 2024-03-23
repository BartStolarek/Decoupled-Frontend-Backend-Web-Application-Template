import React, { useState, useEffect } from 'react';

const Navbar: React.FC = () => {
  const [isMenuOpen, setIsMenuOpen] = useState<boolean>(false);
  const [hasToken, setHasToken] = useState<boolean>(false);

  useEffect(() => {
    // Check for token in local storage and update state accordingly
    const token: string | null = localStorage.getItem('jwtToken');
    setHasToken(!!token);
  }, []);

  const toggleMenu = (): void => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <>
      <nav className="navbar bg-neutral z-10 min-w-full shadow-lg">
        <div className="navbar-start">
          <div
            tabIndex={0}
            className="menu-icon btn btn-ghost btn-small h-6 w-8 mx-3 p-0 min-h-0 z-30 fixed"
            role="button"
            onClick={toggleMenu}
            onKeyDown={toggleMenu}
          >
            <span className="bar shadow-sm text-text bg-text"></span>
            <span className="bar shadow-sm text-text bg-text"></span>
            <span className="bar shadow-sm text-text bg-text"></span>
          </div>
        </div>
        <div className="navbar-center">
          <a className="btn btn-ghost text-3xl text-text">Logo</a>
        </div>
        <div className="navbar-end">
          {hasToken ? (
            <div className="dropdown dropdown-end">
              <div tabIndex={0} role="button" className="btn btn-ghost btn-sm avatar">
                <div className="w-10 rounded-full shadow">
                  <img alt="User Avatar" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
                </div>
              </div>
              <ul tabIndex={0} className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                <li><a>Profile</a></li>
                <li><a>Settings</a></li>
                <li><a>Logout</a></li>
              </ul>
            </div>
          ) : (
            <div className="flex gap-8">
              <a href="/register" className="btn btn-ghost btn-sm w-24 hidden md:block text-lg">Register</a>
              <a href="/login" className="btn btn-secondary btn-sm shadow w-24 hidden md:block">Login</a>
              <a href="/account" className="btn btn-ghost md:hidden flex justify-center items-center">
                {/* Icon or Avatar */}
              </a>
            </div>
          )}
        </div>
      </nav>

      <div className={`${isMenuOpen ? 'translate-x-0' : '-translate-x-full'} fixed inset-0 bg-black bg-opacity-90 backdrop-blur-sm z-20 min-w-full items-top text-white transition-transform duration-300 ease-in-out`}>
        <div className="flex flex-col min-w-full space-y-20 p-10">
          <div className="text-right min-w-full">
            <a href="#" className="text-4xl font-bold">Logo</a>
          </div>
          <div className="space-y-16">
            <a href="#" className="block text-5xl mb-4">Homepage</a>
            <a href="#" className="block text-5xl mb-4">Portfolio</a>
            <a href="#" className="block text-5xl">About</a>
          </div>
        </div>
      </div>
    </>
  );
};

export default Navbar;
