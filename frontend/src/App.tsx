import { Routes, Route } from 'react-router'
import Home from './pages/Home'
import HoneyMap  from './pages/HoneyMap'
import Admin from './pages/Admin'

function App() {

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/map" element={<HoneyMap />} />
      <Route path="/admin" element={<Admin />} />


    </Routes>
  );
}

export default App