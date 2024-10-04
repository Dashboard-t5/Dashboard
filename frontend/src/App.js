import { Routes, Route } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import './globals.css'
import Nav from './components/Nav/Nav'
import Main from './components/Main/Main'
import NotFound from './components/NotFound/NotFound'

function App() {
  return (
    <>
      <Routes>
        <Route exact path='/' index={true}
            element={
                <>
                    <Nav/>
                    <Main type='charts'/>
                </>
            }
        />
        <Route path='/docs'
            element={
                <>
                    <Nav/>
                    <Main type='docs'/>
                </>
            }
        />
        
        <Route path='*' element={<NotFound/>}/>

    </Routes>
    </>
  );
}

export default App;
