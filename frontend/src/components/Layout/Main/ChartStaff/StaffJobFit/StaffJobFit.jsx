import { useState, useEffect, useContext, useCallback } from 'react'
import api from '../../../../../api/api'
import globalStyles from '../../../../../globals.module.css'
import styles from './StaffJobFit.module.css'
import { TeamContext } from "../../../../../context/context"

function StaffJobFit() {
    const [isAllStaff, setAllStaff] = useState([]);
    const { isEmployeeId, setEmployeeId, setSelectedEmployeeName, isTeamId, setTeamTotal } = useContext(TeamContext);

    const getTeam = useCallback(async () => {
        try {
            let data = await api.getTeam(isTeamId)
// console.log(data)
            setAllStaff(data);
            setTeamTotal(data?.length);
        } catch (err) {
            console.error(err);
        }
    }, [isTeamId, setTeamTotal]);

    useEffect(() => {
        getTeam();
    }, [getTeam]);

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
            <table className={globalStyles.table}>
                <tbody>
                {isAllStaff?.length === 0 ? (
                    <tr className={globalStyles.tableRow}>
                        <td colSpan="2" className={globalStyles.tableColLeft}>В меню выберите Команду</td>
                    </tr>
                ) : (
                    isAllStaff.map((employee, i) => (
                        <tr
                            key={i}
                            onClick={() => handleRowClick(employee.employee_id, employee.employee)}
                            className={`${globalStyles.tableRow} ${isEmployeeId === employee.employee_id ? globalStyles.tableRowSelected : ''}`}
                            style={{ cursor: 'pointer' }}
                        >
                            <td className={globalStyles.tableColLeft}>{employee.employee}</td>
                            <td className={globalStyles.tableColRight}>{`${employee.percentage}%`}</td>
                        </tr>
                    ))
                )}
                </tbody>
            </table>
        </>
    );
}

export default StaffJobFit;