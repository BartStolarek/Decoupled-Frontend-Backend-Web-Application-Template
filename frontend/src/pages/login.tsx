import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const LoginPage: React.FC = () => {
  return (
    <>
      <Navbar />
      <div className="global">
        <section className="section">
          <div className="container">
            {/* Placeholder for logo */}
          </div>
        </section>
        <section className="section">
          <div className="container">
            <h2 className="text-center text-2xl font-bold tracking-tight text-text">Sign in to your account</h2>
          </div>
          <div className="container max-w-xl flex flex-col prose">
            <label htmlFor="email" className="text-sm font-medium text-gray-900">Email address</label>
            <input id="email" name="email" type="email" autoComplete="email" className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm" />
            <label htmlFor="password" className="mt-6 text-sm font-medium text-gray-900">Password</label>
            <input id="password" name="password" type="password" autoComplete="current-password" className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm" />
            <a href="#" className="mt-2 text-secondary hover:text-accent sm:text-sm">Forgot password?</a>
          </div>
          <div className="container center">
            <a href="#" className="btn center btn-sm w-24">Login</a>
          </div>
        </section>
      </div>
      <Footer />
    </>
  );
};

export default LoginPage;