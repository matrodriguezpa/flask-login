// src/Protected.js
import React, { useState } from 'react';
import axios from 'axios';

function Protected({ token }) {
  const [message, setMessage] = useState('');

  const fetchProtected = async () => {
    try {
      const response = await axios.get('http://localhost:5000/protected', {
        headers: {
          Authorization: `Bearer ${token}`,  // pass token in header
        },
      });
      setMessage(response.data.logged_in_as);
    } catch (error) {
      console.error('Access denied:', error.response?.data?.message);
    }
  };

  return (
    <div>
      <h2>Protected</h2>
      <button onClick={fetchProtected}>Access Protected Route</button>
      {message && <p>Logged in as: {message}</p>}
    </div>
  );
}

export default Protected;
