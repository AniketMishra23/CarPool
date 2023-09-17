/* eslint-disable no-unused-vars */
import React from 'react';
import Header from './compoenets/Header';
import Landing from './compoenets/Landing';
import Footer from './compoenets/Footer';
import Pool from './compoenets/Pool/Pool';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Pooler from './compoenets/Pooler/Pooler';
import Login from './compoenets/Login';
import Signup from './compoenets/Signup';

function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Header className="flex self-start" />
        <div className="flex-grow">
          <Routes>
            <Route exact path="/" element={<Landing />} />
            <Route exact path="/pool" element={<Pool />} />
            <Route exact path="/pooler" element={<Pooler />} />
            <Route exact path="/login" element={<Login />} />
            <Route exact path="/signup" element={<Signup />} />
          </Routes>
        </div>
        <Footer className="self-end" style={{ position: 'fixed', bottom: 0, left: 0, right: 0 }} />
      </div>
    </Router>
  );
}

export default App;
