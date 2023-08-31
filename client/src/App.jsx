import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import SongList from './components/SongList';
import ChorusGen from './components/ChorusGen';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<ChorusGen />} />
          <Route path="/songs" element={<SongList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
