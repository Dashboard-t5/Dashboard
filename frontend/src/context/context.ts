import React, { Dispatch, SetStateAction } from 'react';


interface TeamContextType {
    teamsIdAndName: [],
    setTeamsIdAndName: Dispatch<SetStateAction<any>>,
    isTeamId: number | null,
    isTeamTotal: number,
    isTeamName: string,
    setTeamName: Dispatch<SetStateAction<string>>,
    allTeamsStaff: [],
    setAllTeamsStaff: Dispatch<SetStateAction<any>>,
    isEmployeeId: number | null,
    selectedEmployeeName: string | '',
    isBusFactor: number,
    setBusFactor: Dispatch<SetStateAction<number>>,
}

// Создаем контекст с дефолтным значением
export const TeamContext = React.createContext<TeamContextType>({
    teamsIdAndName: [],
    setTeamsIdAndName: () => {},
    isTeamId: null,
    isTeamTotal: 0,
    isTeamName: '- - -',
    setTeamName: () => {},
    allTeamsStaff: [],
    setAllTeamsStaff: () => {},
    isEmployeeId: null,
    selectedEmployeeName: '',
    isBusFactor: 0,
    setBusFactor: () => {}, // Заглушка для setBusFactor
});