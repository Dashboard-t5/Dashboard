import React, { Dispatch, SetStateAction } from 'react';

// Тип для контекста
interface TeamContextType {
    isEmployeeId: number | null;
    isTeamId: number | null;
    isTeamTotal: number;
    isBusFactor: number;
    setBusFactor: Dispatch<SetStateAction<number>>; // add function for changes of busFactor
}

// Создаем контекст с дефолтным значением
export const TeamContext = React.createContext<TeamContextType>({
    isEmployeeId: null,
    isTeamId: null,
    isTeamTotal: 0,
    isBusFactor: 0,
    setBusFactor: () => {}, // Заглушка для setBusFactor
});