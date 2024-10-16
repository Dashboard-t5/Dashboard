<<<<<<< HEAD
import { useState, useEffect, useContext, useCallback } from 'react'
=======
import {useState, useEffect, useContext} from 'react'
>>>>>>> front-dev
import axios from 'axios'
import styles from './SkillsLevel.module.css'
import ChartLeftBars from '../../../../Charts/ChartLeftBars'
import { TeamContext } from '../../../../../context/context'
<<<<<<< HEAD
import { DB_URL } from "../../../../../utils/constants";
=======
>>>>>>> front-dev

function SkillsLevel() {
    const { isEmployeeId, isTeamId } = useContext(TeamContext);
    const [isFetchingData, setFetchingData] = useState(false)
    const [isAllSkills, setAllSkills] = useState([])

<<<<<<< HEAD
    const fetchSkills = useCallback(async () => {
        if (!isTeamId) return;

        setFetchingData(true)
        let url = isEmployeeId
            ? `${DB_URL.serverUrl}/api/v1/dashboard/suitability_position/${isEmployeeId}/skills`
            : `${DB_URL.serverUrl}/api/v1/dashboard/skill_level/?team=${isTeamId}`;
=======
    console.log('isEmployeeId, isTeamId:', isEmployeeId, isTeamId)

    useEffect(() => {
        if (isTeamId) {
            fetchSkills();
        }
    }, [isEmployeeId, isTeamId]);
    const fetchSkills = async () => {
        if (!isTeamId) return;

        setFetchingData(true)
        // const db_url = 'https://jsonplaceholder.typicode.com/';
        let url = isEmployeeId
            ? `http://127.0.0.1:8000/api/v1/dashboard/suitability_position/${isEmployeeId}/skills`
            : `http://127.0.0.1:8000/api/v1/dashboard/skill_level/?team=${isTeamId}`;
>>>>>>> front-dev

        try {
            let { data } = await axios.get(`${url}`, {
                headers: {
                    'Accept': 'application/json',
                },
            });
<<<<<<< HEAD
            setAllSkills(data)
            return data;
=======
            console.log(data)
            setAllSkills(data)
            return data;

>>>>>>> front-dev
        } catch (err) {
            console.error(err)
        } finally {
            setFetchingData(false)
        }
<<<<<<< HEAD
    }, [isEmployeeId, isTeamId]);

    useEffect(() => {
        if (isTeamId) {
            fetchSkills();
        }
    }, [isTeamId, fetchSkills]);
=======
    }
>>>>>>> front-dev

    return (
        <div>
            <p className={styles.chartSubtitle}>
                {isEmployeeId ? 'ШКАЛЫ УРОВНЕЙ НАВЫКОВ СОТРУДНИКА' : 'СРЕДНИЕ УРОВНИ НАВЫКОВ КОМАНДЫ'}
            </p>

            {isFetchingData ? (
                <p>Loading...</p>
            ) : (
                <ChartLeftBars key={isEmployeeId || 'team'} data={isAllSkills}/>
            )}
        </div>
    )
}

export default SkillsLevel