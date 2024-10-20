import {useContext, useState} from 'react';
import globalStyles from '../../../../globals.module.css'
import styles from './ChartStaff.module.css';
import StaffJobFit from './StaffJobFit/StaffJobFit';
import StaffSkilledNum from './StaffSkilledNum/StaffSkilledNum';
import { TeamContext } from '../../../../context/context'

function ChartStaff() {
    const { selectedEmployeeName } = useContext(TeamContext);
    const [activeTab, setActiveTab] = useState('skillsLevel');

    return (
        <section id='chartStaff' className={`${globalStyles.chart} ${styles.chartStaff}`}>

            <div className={styles.tabsChart}>
                <div
                    className={`${styles.tabChart} ${activeTab === 'skillsLevel' ? styles.active : ''}`}
                    onClick={() => setActiveTab('skillsLevel')}
                >
                    <p>Соответствие должности</p>
                </div>

                <div
                    className={`${styles.tabChart} ${activeTab === 'staffNums' ? styles.active : ''}`}
                    onClick={() => setActiveTab('staffNums')}
                >
                    Количество сотрудников, владеющих навыками
                </div>
            </div>

            <div className={styles.tabContentChart}>

                <p className={styles.tableSubtitle}>
                    Сотрудник:
                      <span className={styles.tableSubtitleSpan}>{selectedEmployeeName || '[ НЕ ВЫБРАН ]'}</span>
                      • Уровень владения навыками
                </p>

                <div className={styles.scrollableContent}>
                    {activeTab === 'skillsLevel' ? <StaffJobFit/> : <StaffSkilledNum/>}
                </div>
            </div>

        </section>
    );
}

export default ChartStaff;