/* eslint-disable no-unused-vars */
import React, { useState } from 'react';

function Signup() {
  const [formData, setFormData] = useState({
    name: '',
    phoneNumber: '',
    password: '',
    drivingLicense: '',
  });

  const [userType, setUserType] = useState('pooler');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add code here to send the formData and userType to your server for registration.
    console.log(formData, userType);
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h2 className="text-2xl font-semibold text-center mb-6">Signup</h2>
        <div className="flex justify-evenly">
          <button
            className={`${
              userType === 'pooler' ? 'bg-blue-600 text-white' : 'border-2 border-blue-600 text-blue-600'
            } px-4 py-2 rounded-lg`}
            onClick={() => setUserType('pooler')}
          >
            Pooler
          </button>
          <button
            className={`${
              userType === 'pool' ? 'bg-blue-600 text-white' : 'border-2 border-blue-600 text-blue-600'
            } px-4 py-2 rounded-lg`}
            onClick={() => setUserType('pool')}
          >
            Pool
          </button>
        </div>
        <form onSubmit={handleSubmit} className={userType === 'pool' ? 'hidden' : 'block'}>
          <div className="mb-4">
            <label htmlFor="name" className="block text-gray-700 text-sm font-medium">
              Name:
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="phoneNumber" className="block text-gray-700 text-sm font-medium">
              Phone Number:
            </label>
            <input
              type="text"
              id="phoneNumber"
              name="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-gray-700 text-sm font-medium">
              Password:
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="drivingLicense" className="block text-gray-700 text-sm font-medium">
              Driving License:
            </label>
            <input
              type="text"
              id="drivingLicense"
              name="drivingLicense"
              value={formData.drivingLicense}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
              required
            />
          </div>
          <div className="text-center">
            <button
              type="submit"
              className="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 focus:outline-none"
            >
              Signup
            </button>
          </div>
        </form>
        <form onSubmit={handleSubmit} className={userType === 'pooler' ? 'hidden' : 'block'}>
        <div className="mb-4">
            <label htmlFor="name" className="block text-gray-700 text-sm font-medium">
              Name:
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="phoneNumber" className="block text-gray-700 text-sm font-medium">
              Phone Number:
            </label>
            <input
              type="text"
              id="phoneNumber"
              name="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-gray-700 text-sm font-medium">
              Password:
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
              required
            />
          </div>
          <div className="text-center">
            <button
              type="submit"
              className="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 focus:outline-none"
            >
              Signup
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Signup;
