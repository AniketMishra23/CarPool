/* eslint-disable no-unused-vars */
import React , { useState } from 'react';

function Login() {
    const [poolPasswordVisible, setPoolPasswordVisible] = useState(false);
    const passwordToggle = () => {
        setPoolPasswordVisible(!poolPasswordVisible)
    }
    return (
        <div className="flex justify-center mt-28 min-h-screen">
            <div className="w-full max-w-md">
                <div className="mb-8 text-center">
                    <h1 className="text-2xl font-semibold">Login</h1>
                </div>
                <div className="">
                    {/* Pool Login */}
                    <div className="bg-gray-100 p-4 rounded-lg shadow">
                        <form>
                            <div className="mb-4">
                                <label className="block text-gray-700 text-sm font-medium mb-2" htmlFor="poolUsername">
                                    Username:
                                </label>
                                <input
                                    type="text"
                                    id="poolUsername"
                                    name="poolUsername"
                                    className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
                                />
                            </div>
                            <div className="mb-4">
                                <label className="block text-gray-700 text-sm font-medium mb-2" htmlFor="poolPassword">
                                    Password:
                                </label>
                                <input
                                    type={poolPasswordVisible ? 'text' : 'password'}
                                    id="poolPassword"
                                    name="poolPassword"
                                    className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
                                />
                                <input type="checkbox" onClick={passwordToggle}/> <span className='text-sm text-gray-600'>Show Password</span>
                            </div>
                            <div className="text-center">
                                <button
                                    type="submit"
                                    className="bg-blue-500 text-white rounded-full px-4 py-2 hover:bg-blue-600"
                                >
                                    Login
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Login;
