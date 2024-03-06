import React, { useState } from 'react';
import axios from 'axios';

function CheckinComponent() {
  const [user, setUser] = useState('');
  const [task, setTask] = useState('');
  const [message, setMessage] = useState('');

  const handleCheckIn = () => {
    // Construct the API endpoint with query parameters
    const apiUrl = `http://localhost:8000/${user}/checkin/${task}`;
    
    

    // Use axios to make the GET request
    axios.get(apiUrl)
      .then(response => {
        setMessage(response.data);
      })
      .catch(error => {
        setMessage('Failed to check in: ' + (error.response?.data?.detail || error.message));
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
      <input
        type="text"
        placeholder="Task"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button onClick={handleCheckIn}>Checkin</button>
      {message}
    </div>
  );
}

export default CheckinComponent;