import PopupWithForm from '../PopupWithForm'
import styles from './PopupMainMenu.module.css'
import { useContext, useEffect } from "react"
import { TeamContext } from "../../../context/context"
import api from "../../../api/api"

function PopupMainMenu({ onOpen, onClose, name, onSubmit, textBtn }) {
    const { teamsIdAndName, setTeamsIdAndName, isTeamId, setTeamId, isTeamName, setTeamName,
        allTeamsStaff, setAllTeamsStaff, isEmployeeId, setEmployeeId, selectedEmployeeName, setSelectedEmployeeName} = useContext(TeamContext);
    // const [ teamsIdAndName, setTeamsIdAndName ] = useState([])

    // Получаем список команд при монтировании компонента
    useEffect(() => {
        const fetchTeams = async () => {
            try {
                const data = await api.getTeamNames();
                setTeamsIdAndName(data);
            } catch (err) {
                console.error('Error fetching teams',err)
            }
        }

        fetchTeams()
    },[])

    // Получаем список всех сотрудников при монтировании компонента
    useEffect(() => {
        const fetchAllStaff = async () => {
            try {
                const data = await api.getAllEmployees();

                // В контекст устанавливаем список всех сотрудников
                setAllTeamsStaff(data);
          console.log(data)
            } catch (err) {
                console.error('Error fetching teams',err)
            }
        }
        fetchAllStaff()
    },[])

    // Обработчик изменения выбора команды через select
    const handleTeamChange = (teamId) => {
        const numericTeamId = Number(teamId)

        // В контекст устанавливаем id выбранной команды (teamId)
        setTeamId(numericTeamId)

        // В контекст устанавливаем имя выбранной команды
        const selectedTeam = teamsIdAndName.find(team => team.id === numericTeamId)
      console.log(teamsIdAndName)
        if (selectedTeam) {
            setTeamName(selectedTeam.name)
        }
    }

    // Обработчик изменения выбора сотрудника через select
    const handleEmployeeChange = (employeeId) => {
        const numericEmployeeId = Number(employeeId)

        // В контекст устанавливаем id выбранного сотрудника
        setEmployeeId(numericEmployeeId)

        // В контекст устанавливаем имя выбранного сотрудника
        const selectedEmployee = allTeamsStaff.find(employee => Number(employee.employee_id) === numericEmployeeId)

      console.log(selectedEmployee)
        if (selectedEmployee) {
            setSelectedEmployeeName(selectedEmployee.employee)
            console.log(selectedEmployeeName)
        }
    }

    // console.log(onOpen)
    return (
        <PopupWithForm
            name={name}
            onSubmit={onSubmit}
            onOpen={onOpen}
            onClose={onClose}
            textBtn={textBtn}
        >
            <p>children...</p>

            <div className={styles.selectContainer}>
                <select
                    name='team'
                    value={isTeamId || ''}
                    onChange={(e) => handleTeamChange(e.target.value)}
                    className={styles.select}
                >
                    <option value="" className={styles.optionDefault}>--Команда--</option>
                    {teamsIdAndName.map((team) => (
                        <option key={team.id} value={team.id} className={styles.option}>
                            {team.name}
                        </option>
                    ))}
                </select>

                <select
                    name='employee'
                    value={isEmployeeId || ''}
                    onChange={(e) => handleEmployeeChange(e.target.value)}
                    className={styles.select}
                >
                    <option value="" className={styles.optionDefault}>--Сотрудник--</option>
                    {allTeamsStaff.map((allStaff) => (
                        <option key={allStaff.employee_id} value={allStaff.employee_id} className={styles.option}>
                            {allStaff.employee}
                        </option>
                    ))}
                    {/*<option value='employee' className={styles.option}>{'Иванов'}</option>*/}
                    {/*<option value='employee' className={styles.option}>{'Петров'}</option>*/}
                    {/*<option value='employee' className={styles.option}>{'Другой сотрудник'}</option>*/}
                </select>

            </div>
        </PopupWithForm>
    )
}

export default PopupMainMenu;