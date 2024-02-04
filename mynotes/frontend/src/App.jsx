import {
  BrowserRouter as Router,
  // Routes is imported to solve the error of blank pages
  // All Route must be inside of Routes for the pages not to be blank
  Routes,
  Route,
  useNavigate
} from "react-router-dom"

import Header from './components/Header'
import NotesListPage from './pages/NotesListPage'
import NotePage from './pages/NotePage'

import './App.css';

function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
          <Header />
          <Routes>
            <Route path="/" element={<NotesListPage />} />
            <Route path="/note/:id" element={<NotePage />} />
          </Routes>
          </div>
      </div>
    </Router>
  );
}


export default App;