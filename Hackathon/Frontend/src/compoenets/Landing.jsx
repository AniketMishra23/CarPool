/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { Link } from "react-router-dom"

function Landing() {
  const [slideRight, setSlideRight] = useState(false);
  const [slideLeft, setSlideLeft] = useState(false);

  const handleSlideRight = () => {
    setSlideRight(true);
  };

  const handleSlideLeft = () => {
    setSlideLeft(true);
  };

  return (
    <div className={`flex justify-between items-center h-screen ${slideLeft ? 'slide-left' : ''}`}>
      <div className={`w-[50%] border-r-2 h-full flex items-center justify-center border-black/10 ${slideRight ? 'slide-right' : ''} `}>
      <Link to='/pool' className="bg-blue-500 text-white px-4 py-2 rounded mb-4" onClick={handleSlideRight}>
        I Have a Car
      </Link>
      </div>
      <div className='w-[50%] h-full flex items-center justify-center'>
      <Link to='/pooler' className="bg-green-500 text-white px-4 py-2 rounded" onClick={handleSlideLeft}>
        I Need a Ride
      </Link>
      </div>
    </div>
  );
}

export default Landing;
