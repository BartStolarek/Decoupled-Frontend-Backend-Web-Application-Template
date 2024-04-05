import React, { useState } from 'react';
import { useRouter } from 'next/router';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const RegisterPage: React.FC = () => {

  const router = useRouter();

  const [formData, setFormData] = useState({
    firstname: '',
    lastname: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // Perform form validation
    if (formData.password !== formData.confirmPassword) {
      alert('Passwords do not match');
      return;
    }

    try {
      const API_URL = process.env.NEXT_PUBLIC_API_URL;
      const response = await fetch(`${API_URL}/api/user/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          first_name: formData.firstname,
          last_name: formData.lastname,
          email: formData.email,
          password: formData.password,
        }),
      });

      if (response.ok) {
        router.push('/login');
      } else {
        const data = await response.json();
        alert(`Registration failed: ${data.message}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred during registration');
    }
  };

  return (
    <>
      <Navbar />
      <div className="global">
        <section className="section">
          <div className="container">{/* Placeholder for logo */}</div>
        </section>
        <section className="section">
          <div className="container">
            <h2 className="text-center text-2xl font-bold tracking-tight text-text">
              Register an account
            </h2>
          </div>
          <form onSubmit={handleSubmit} className="container max-w-xl flex flex-col prose">
            {/* First Name */}
            <label htmlFor="firstname" className="text-sm font-medium text-gray-900">
              First Name
            </label>
            <input
              id="firstname"
              name="firstname"
              type="text"
              value={formData.firstname}
              onChange={handleChange}
              className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm"
            />

            {/* Last Name */}
            <label htmlFor="lastname" className="mt-6 text-sm font-medium text-gray-900">
              Last Name
            </label>
            <input
              id="lastname"
              name="lastname"
              type="text"
              value={formData.lastname}
              onChange={handleChange}
              className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm"
            />

            {/* Email */}
            <label htmlFor="email" className="mt-6 text-sm font-medium text-gray-900">
              Email address
            </label>
            <input
              id="email"
              name="email"
              type="email"
              autoComplete="email"
              value={formData.email}
              onChange={handleChange}
              className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm"
            />

            {/* Password */}
            <label htmlFor="password" className="mt-6 text-sm font-medium text-gray-900">
              Password
            </label>
            <input
              id="password"
              name="password"
              type="password"
              autoComplete="current-password"
              value={formData.password}
              onChange={handleChange}
              className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm"
            />

            {/* Verify Password */}
            <label htmlFor="confirmPassword" className="mt-6 text-sm font-medium text-gray-900">
              Confirm Password
            </label>
            <input
              id="confirmPassword"
              name="confirmPassword"
              type="password"
              value={formData.confirmPassword}
              onChange={handleChange}
              className="mt-2 input input-sm rounded input-bordered focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm"
            />

            <div className="container center">
              <button type="submit" className="btn center btn-sm w-24">
                Register
              </button>
            </div>
          </form>
        </section>
      </div>
      <Footer />
    </>
  );
};

export default RegisterPage;