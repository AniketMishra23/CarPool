/* eslint-disable no-unused-vars */
import React, { useState } from "react";
import Map from "../Map";
import axios from "axios";

export default function App() {
  const [location, setLocation] = useState("");
  const [destination, setDestination] = useState("");
  const [googleMapsUrl, setGoogleMapsUrl] = useState("");
  const [showMap, setShowMap] = useState(false);


  const cardContainerStyle = {
    maxHeight: '350px', // Set the maximum height for the scrollable area
    overflowY: 'scroll', // Use 'scroll' to always show the scrollbar
    scrollbarWidth: 'none', // Use 'thin' for a thin scrollbar
    scrollbarColor: 'rgba(0, 0, 0, 0.3) rgba(0, 0, 0, 0.1)',
  };

  const cardStyle = {
    border: '2px solid rgba(0, 0, 0, 0.3)',
    borderRadius: '8px',
    margin: '8px 0',
    padding: '8px',
  };
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Make a POST request to your API endpoint to get Google Maps URL.
      const response = await axios.post('http://127.0.0.1:5000/api/map', { lat: location, lang: destination });

      // Assuming your API response contains a 'google_maps_url' field.
      setGoogleMapsUrl(response.data.google_maps_url);
      setShowMap(true);
    } catch (error) {
      console.error(error);
    }
  };
  const pools = [
    {
      user: "Pal",
      age: "21",
      gender: "Male",
      from: "Bhaynder",
      to: "Goa"
    },
    {
      user: "Pal",
      age: "21",
      gender: "Male",
      from: "Bhaynder",
      to: "Goa"
    },
    {
      user: "Pal",
      age: "21",
      gender: "Male",
      from: "Bhaynder",
      to: "Goa"
    }
  ]

  return (
    <div className="min-h-[calc(100vh-32px-32px)]">
      <h1 className="text-3xl font-bold text-center my-4">
        Pooler can Get the Customer
      </h1>
      <div className="flex">
        <div className="w-[50%] ml-10">
          <form onClick={handleSubmit} className=" space-y-4">
            <div>
              <label htmlFor="location" className="text-lg font-semibold text-black/80">
                Location:
              </label><br />
              <input
                type="text"
                id="location"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                className="border-2 w-1/2 h-10 border-black/50 outline-none p-4 rounded-md"
                required
              />
            </div>
            <div>
              <label htmlFor="destination" className="text-lg font-semibold text-black/80">
                Destination:
              </label><br />
              <input
                type="text"
                id="destination"
                value={destination}
                className="border-2 w-1/2 h-10 border-black/50 outline-none p-4 rounded-md"
                onChange={(e) => setDestination(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded-full">
              Get A Pools
            </button>
          </form>
          <div className="mt-7 -ml-9 border-b-2 w-[60%] border-black" />
          <div className="bottom">
            <p className="mt-3 text-xl">Pools Avilability :-</p>
            <div style={cardContainerStyle}>
              {pools.map((card, index) => {
                return (
                  <div className="cards w-[50%] border-2 border-black/[0.3] rounded-md my-2 shadow-lg" key={index} style={cardStyle}>
                    <div className="flex justify-between p-4 font-semibold text-base max-h-10">
                      <p>{card.user}</p>
                      <p>{card.gender}</p>
                      <p>{card.age}</p>
                    </div>
                    <div className="flex justify-between items-center p-4">
                      <p>{card.from}</p>
                      <p>{card.to}</p>
                      <a href="/" className="border-2 border-white/[0.3] py-1 px-2 rounded-md bg-blue-500 text-white hover:bg-blue-600">Contact</a>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>
        </div>
          <div className="w-[50%] border-2 border-black h-[calc(100vh-192px)]">
            {/* Display the Google Maps URL or integrate Google Maps here */}
            <Map />
          </div>
      </div>
    </div>
  );
}
