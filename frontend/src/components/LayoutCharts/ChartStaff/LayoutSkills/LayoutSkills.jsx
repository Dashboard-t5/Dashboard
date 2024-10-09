import {useState, useEffect} from 'react'
import axios from 'axios'
import './LayoutSkills.css'

function LayoutSkills() {
    const [isFetchingData, setFetchingData] = useState('false')
    const [isAllStaff, setAllStaff] = useState([])

    const fetchAllStaff = async () => {
        setFetchingData(true)
        const db_url = 'https://jsonplaceholder.typicode.com/';
        // const db_url = 'http://127.0.0.1:8000/api/v1/dashboard/suitability_position/?team=5';
        try {
            let { data } = await axios.get(`${db_url}albums`, {
                headers: {
                    'Accept': 'application/json',
                },
            });
            console.log(data)
            setAllStaff(data)
            return data;

        } catch (err) {
            console.error(err)
        } finally {
            setFetchingData(false)
        }
    }

    const handleFetchClick = () => {
        fetchAllStaff()
    }

    return (
        <div>
            <p className='chart__subtitle'>Сотрудник: ${}_ • Уровень владения навыками</p>

            {/*TEST FETCH BTN*/}
            <button onClick={() => handleFetchClick()} className='TEST-BTN'>Get Data to Console</button>

            <table className='chart__table'>
                <thead>
                    <tr>
                        <th className='table__header'>Сотрудник</th>
                        <th>Доля навыков с удовлетворительной оценкой</th>
                    </tr>
                </thead>

                <tbody>
                <tr>
                    <td>Ефремов Вячеслав</td>
                    <td>79%</td>
                </tr>
                {isAllStaff.length === 0 ? (
                        <tr>
                            <td colSpan="2">Загрузить...</td>
                        </tr>
                    ) : (
                        isAllStaff.map((staff, i) => (
                            <tr key={i}>
                                <td>{staff.id}</td>
                                <td>{staff.title}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>

            {/*TEST FETCH BTN*/}
            {/*<button onClick={() => handleFetchClick()} className='TEST-BTN'>Get Data to Console</button>*/}

            {/*<ul>*/}
            {/*    {isAllStaff.length === 0 ? (*/}
            {/*        <li>*/}
            {/*            <p>Загрузить...</p>*/}
            {/*        </li>*/}
            {/*    ) : (*/}

            {/*        console.log(isAllStaff)*/}

            {/*    )}*/}
            {/*</ul>*/}

        </div>
    )
}

export default LayoutSkills