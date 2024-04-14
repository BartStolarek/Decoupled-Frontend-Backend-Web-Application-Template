import React, { useState } from 'react';
import { useRouter } from 'next/router';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import jwt_decode from "jwt-decode";


const LoginPage: React.FC = () => {
  const router = useRouter();

  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  function parseJwt(token: string) {
    if (!token) { return; }
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace('-', '+').replace('_', '/');
    return JSON.parse(window.atob(base64));
    }

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const API_URL = process.env.NEXT_PUBLIC_API_URL;
      const response = await fetch(`${API_URL}/api/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          password: formData.password,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        console.log(`Token received: ${data.data.user_token}`)
        // Store the token in localStorage
        localStorage.setItem('user_token', data.data.user_token); // Assuming the token is returned in the response body under 'token'
        
        
        // Decode the token to read the user's role
        const decodedToken = parseJwt(data.data.user_token);
        const userRole = decodedToken.user_role;

        // Optionally, store the role in localStorage for quick access
        localStorage.setItem('user_role', userRole);

        router.push('/'); // Redirect to the homepage or dashboard as needed
      } else {
        alert(`Login failed: ${data.message}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred during login');
    }
  };

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
            <a href="#" className="mt-2 text-secondary hover:text-accent text-sm block md:hidden">Register?</a>
          </div>
          <form onSubmit={handleSubmit} className="container max-w-xl flex flex-col prose">
            <label htmlFor="email" className="text-sm font-medium text-gray-900">Email address</label>
            <input id="email" name="email" type="email" autoComplete="email" value={formData.email} onChange={handleChange} className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm" />
            <label htmlFor="password" className="mt-6 text-sm font-medium text-gray-900">Password</label>
            <input id="password" name="password" type="password" autoComplete="current-password" value={formData.password} onChange={handleChange} className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm" />
            <a href="#" className="mt-2 text-secondary hover:text-accent text-sm">Forgot password?</a>
            <div className="container center">
              <button type="submit" className="btn center btn-sm w-24">
                Login
              </button>
            </div>
          </form>
        </section>
      </div>
      <Footer />
    </>
  );
};

export default LoginPage;
