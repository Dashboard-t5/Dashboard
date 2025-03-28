import {useContext, useState} from 'react';
import globalStyles from '../../../../globals.module.css'
import styles from './ChartStaff.module.css';
import StaffJobFit from './StaffJobFit/StaffJobFit';
import StaffSkilledNum from './StaffSkilledNum/StaffSkilledNum';
import { AppContext } from '../../../../context/context'

function ChartStaff() {
    const { teams, isTeamName, selectedEmployee, selectedPosition} = useContext(AppContext);
    const [ activeTab, setActiveTab ] = useState('staffJobFit');

 // console.log('isTeamName, teams', "selectedEmployee:", isTeamName, teams, selectedEmployee)
 // console.log('selectedPosition, selectedEmployee::',selectedPosition, selectedEmployee)

    // функция для отображения в поле Должность •
  const getSelectedPosition = (selectedPosition, selectedEmployee) => {
    if (selectedPosition && selectedPosition.name) {
      return selectedPosition.name;
    }

    if (selectedEmployee && selectedEmployee.position) {
      return selectedEmployee.position;
    }

    // Если ничего не найдено
    return '[ НЕ ВЫБРАНА ]';
  };

    return (
        <section id='chartStaff' className={`${globalStyles.chart} ${styles.chartStaff}`}>

            <div className={globalStyles.tabsChart}>

              {/* 1-st tab */}
                <div className={`${globalStyles.tabChart} ${activeTab === 'staffJobFit' ? globalStyles.active : ''}`}
                     onClick={() => setActiveTab('staffJobFit')}
                >
                    <p>Соответствие должности</p>
                    {activeTab === 'staffJobFit'
                        ? <div className={globalStyles.chartSubtitles}>
                        <p className={globalStyles.chartSubtitle}>
                          Сотрудник •
                          <span
                            className={globalStyles.chartSubtitleSpan}>{Object.keys(selectedEmployee).length === 0 ? '[ НЕ ВЫБРАН ]' : `${selectedEmployee.last_name} ${selectedEmployee.first_name}`}
                                </span>
                        </p>
                        <p className={globalStyles.chartSubtitle}>
                          Команда •
                          <span
                            className={globalStyles.chartSubtitleSpan}>{ isTeamName || '[ НЕ ВЫБРАНА ]'}
                                </span>
                        </p>
                        <p className={globalStyles.chartSubtitle}>
                          Должность •
                          <span
                            // className={globalStyles.chartSubtitleSpan}>{ console.log('selectedPosition',selectedPosition) || '[ НЕ ВЫБРАНА ]'}
                              className={globalStyles.chartSubtitleSpan}>
                                { getSelectedPosition(selectedPosition, selectedEmployee) }
                          </span>
                        </p>
                      </div>
                      :
                      <p
                        className={`${globalStyles.chartSubtitle} ${activeTab !== 'staffJobFit' ? globalStyles.active : ""}`}>
                        Другое •
                      </p>
                    }
                </div>

              {/* 2-nd tab */}
              <div className={`${globalStyles.tabChart} ${activeTab === 'staffNums' ? globalStyles.active : ''}`}
                     onClick={() => setActiveTab('staffNums')}
                >
                    <p>Количество сотрудников, владеющих навыками</p>
                </div>
            </div>


            {/* sub-chart content */}
            <div className={globalStyles.tabContentChart}>

                {activeTab === 'staffJobFit'
                    ? <p className={`${globalStyles.tableHeader}`}>
                        Доля навыков с удовлетворительной оценкой
                    </p>
                    : ""
                }

                <div className={globalStyles.scrollableContent}>
                    {activeTab === 'staffJobFit' ? <StaffJobFit/> : <StaffSkilledNum/>}
                </div>
            </div>

        </section>
    );
}

export default ChartStaff;