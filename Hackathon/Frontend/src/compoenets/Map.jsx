/* eslint-disable no-unused-vars */
import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const Map = () => {
  const mapCenter = [51.505, -0.09]; // Initial map center (latitude, longitude)

  return (
    <MapContainer
      center={mapCenter}
      zoom={13}
      style={{ width: '100%', height: '1000px' }}
    >
      {/* Add a tile layer using OpenStreetMap */}
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {/* Add a marker with a popup */}
      <Marker position={mapCenter}>
        <Popup>
          A sample popup. <br /> You can add your content here.
        </Popup>
      </Marker>
    </MapContainer>
  );
};

export default Map;
