import './App.css';
import CheckinComponent from './components/checkin';
import CheckoutComponent from './components/checkout';
import ReportComponent from './components/report';

function App() {
  return (
    <div className="App">
      <CheckinComponent/>
      <CheckoutComponent/>
      <ReportComponent/>
    </div>
  );
}

export default App;
