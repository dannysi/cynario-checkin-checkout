import React, { useState } from 'react';
import axios from 'axios';

function ReportComponent() {
  const [reportData, setReportData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFetchReport = async () => {
    setIsLoading(true);
    setError('');
    try {
      const response = await axios.get('http://localhost:8000/report');
      setReportData(response.data);
    } catch (err: any) {
      setError('Failed to fetch report data: ' + (err.response?.data?.detail || err.message));
    }
    setIsLoading(false);
  };

  return (
    <div>
      <h2>Task Report</h2>
      <button onClick={handleFetchReport} disabled={isLoading}>
        {isLoading ? 'Loading...' : 'Get Report'}
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {Object.entries(reportData).map(([user, tasks]:any) => (
          <li key={user}>
            <strong>{user}</strong>
            <ul>
              {tasks.map((task:any, index:any) => (
                <li key={index}>
                  {task.name} - {task.duration}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReportComponent;
