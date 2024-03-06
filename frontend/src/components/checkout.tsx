import React, { useState } from 'react';
import axios from 'axios';

function CheckoutComponent() {
  const [user, setUser] = useState('');
  const [message, setMessage] = useState('');

  const handleCheckout = () => {
    // Construct the API endpoint with query parameters
    const apiUrl = `http://localhost:8000/${user}/checkout`;
    
    // Use axios to make the GET request
    axios.get(apiUrl)
      .then(response => {
        setMessage(response.data);
      })
      .catch(error => {
        setMessage('Failed to checkout: ' + (error.response?.data?.detail || error.message));
      });
  };

  return (
    <div>
      <input
        type="text"
        placeholder="User"
        value={user}
        onChange={(e) => setUser(e.target.value)}
      />
      <button onClick={handleCheckout}>Checkout</button>
      {message}
    </div>
  );
}

export default CheckoutComponent;