import { Routes, Route } from 'react-router-dom'
import {useState} from 'react'
import Layout from './components/Layout/Layout'
import NotFound from './components/NotFound/NotFound'
import { TeamContext } from './context/context';

function App() {
  const [teamsIdAndName, setTeamsIdAndName] = useState([])
  const [isTeamId, setTeamId] = useState(5)
  const [isTeamName, setTeamName] = useState('')
  const [isTeamTotal, setTeamTotal] = useState(0)
  const [allTeamsStaff, setAllTeamsStaff] = useState([])
  const [isEmployeeId, setEmployeeId] = useState(null)
  const [selectedEmployeeName, setSelectedEmployeeName] = useState('')
  const [isBusFactor, setBusFactor] = useState(0)

  return (
      <>
        <TeamContext.Provider value={{
          teamsIdAndName,
          setTeamsIdAndName,
          isTeamId,
          setTeamId,
          isTeamName,
          setTeamName,
          isTeamTotal,
          setTeamTotal,
          allTeamsStaff,
          setAllTeamsStaff,
          isEmployeeId,
          setEmployeeId,
          selectedEmployeeName,
          setSelectedEmployeeName,
          isBusFactor,
          setBusFactor
        }}
        >
          <Routes>
            <Route exact path='/' index={true}
                   element={<Layout/>}>
            </Route>
            <Route path='*' element={<NotFound/>}/>
          </Routes>
        </TeamContext.Provider>
      </>
  );
}

export default App;
