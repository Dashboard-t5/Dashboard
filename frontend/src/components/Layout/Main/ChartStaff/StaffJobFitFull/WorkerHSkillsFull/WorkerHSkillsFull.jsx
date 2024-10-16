import {useState} from 'react'
import axios from 'axios'
import './StaffJobFitFull.module.css'
import ChartRightBars from "../../../../../Charts/ChartRightBars";

function WorkerSkillsFull() {
    const [isFetchingData, setFetchingData] = useState('false')
    const [isAllStaff, setAllStaff] = useState([])

    const fetchAllStaff = async () => {
        setFetchingData(true)
        const db_url = 'https://jsonplaceholder.typicode.com';
        // const db_url = 'http://127.0.0.1:8000/api/v1/dashboard/suitability_position/?team=5';
        try {
            let { data } = await axios.get(`${db_url}/posts`, {
                headers: {
                    'Accept': 'application/json',
                },
            });
<<<<<<< HEAD
=======
            console.log(data)
>>>>>>> front-dev
            setAllStaff(data)
            return data;

        } catch (err) {
            console.error(err)
        } finally {
            setFetchingData(false)
        }
    }

<<<<<<< HEAD
=======
    const handleFetchClick = () => {
        fetchAllStaff()
    }

>>>>>>> front-dev
    return (
        <div>
            <p className='chart__subtitle'>НА ВСЮ СТРАНИЦУ ТАБЛИЦА: 1. Сотрудник, 2. Доля навыков...</p>

<<<<<<< HEAD
            <ChartRightBars/>

=======

            <ChartRightBars/>


            {/* TEST FETCH BTN */}
            <button onClick={() => handleFetchClick()} className='TEST-BTN'>Get Data to Console</button>

            <ul>
                {isAllStaff.length === 0 ? (
                    <li>
                        <p>Загрузить...</p>
                    </li>
                ) : (
                    console.log(isAllStaff)
                )}
            </ul>

>>>>>>> front-dev
        </div>
    )
}

export default WorkerSkillsFull