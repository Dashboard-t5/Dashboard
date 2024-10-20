import { useState, useEffect, useContext, useCallback } from 'react';
import axios from 'axios';
import styles from './StaffJobFit.module.css';
import { TeamContext } from "../../../../../context/context";
import { DB_URL } from '../../../../../utils/constants'

function StaffJobFit() {
    const [isAllStaff, setAllStaff] = useState([]);
    const { isEmployeeId, setEmployeeId, setSelectedEmployeeName, isTeamId, setTeamTotal } = useContext(TeamContext);

    const getAllStaff = useCallback(async () => {
        const db_url = `${DB_URL.serverUrl}/api/v1/dashboard/suitability_position/?team=${isTeamId}`;
        try {
            let { data } = await axios.get(`${db_url}`, {
                headers: {
                    'Accept': 'application/json',
                },
            });
            setAllStaff(data);
            setTeamTotal(data.length);
        } catch (err) {
            console.error(err);
        }
    }, [isTeamId, setTeamTotal]);

    useEffect(() => {
        getAllStaff();
    }, [getAllStaff]);

    const handleRowClick = useCallback((clickedEmployeeId, clickedEmployeeName) => {
        if (clickedEmployeeId === isEmployeeId) {
            setEmployeeId(null);
            setSelectedEmployeeName('');
        } else {
            setEmployeeId(clickedEmployeeId);
            setSelectedEmployeeName(clickedEmployeeName);
        }
    }, [isEmployeeId, setEmployeeId]);

    return (
        <>
            <table className={styles.table}>
                <thead className={styles.tableHeaders}>
                <tr className={styles.tableRow}>
                    <th className={`${styles.tableHeader} ${styles.tableHeaderLeft}`}>Сотрудник</th>
                    <th className={`${styles.tableHeader} ${styles.tableHeaderRight}`}>
                        Доля навыков с удовлетворительной оценкой
                    </th>
                </tr>
                </thead>

                <tbody>
                {isAllStaff.length === 0 ? (
                    <tr className={styles.tableRow}>
                        <td colSpan="2" className={styles.tableColLeft}>В меню выберите Команду</td>
                    </tr>
                ) : (
                    isAllStaff.map((employee, i) => (
                        <tr
                            key={i}
                            onClick={() => handleRowClick(employee.employee_id, employee.employee)}
                            className={`${styles.tableRow} ${isEmployeeId === employee.employee_id ? styles.tableRowSelected : ''}`}
                            style={{ cursor: 'pointer' }}
                        >
                            <td className={styles.tableColLeft}>{employee.employee}</td>
                            <td className={styles.tableColRight}>{`${employee.percentage}%`}</td>
                        </tr>
                    ))
                )}
                </tbody>
            </table>
        </>
    );
}

export default StaffJobFit;