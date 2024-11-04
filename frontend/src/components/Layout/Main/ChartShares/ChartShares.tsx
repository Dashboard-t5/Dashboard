import {useContext, useState} from 'react';
import globalStyles from '../../../../globals.module.css'
import styles from './ChartShares.css';
import { TeamContext } from '../../../../context/context'

function ChartShares() {
    const [activeTab, setActiveTab] = useState('staffPositions');

    return (
        <section id='StaffPositions' className={`${globalStyles.chart}`}>

            <div className={globalStyles.tabsChart}>
                <div
                    className={`${globalStyles.tabChart} ${activeTab === 'staffPositions' ? globalStyles.active : ''}`}
                    onClick={() => setActiveTab('staffPositions')}
                >
                    <p>Должности сотрудников</p>
                </div>

                <div
                    className={`${globalStyles.tabChart} ${activeTab === 'staffGradesNum' ? globalStyles.active : ''}`}
                    onClick={() => setActiveTab('staffGradesNum')}
                >
                    <p>Количество сотрудников по грейдам</p>
                </div>
            </div>

            {/* sub-chart content */}
            <div className={globalStyles.tabContentChart}>

                {activeTab === 'staffPositions'
                    ? <p className={styles.chartSubtitle}>Должность • </p>
                    : <p className={styles.chartSubtitle}>Грейд • </p>
                }

                <div className={''}>
                    {/*{activeTab === 'staffPositions' ? <Shares/> : <StaffGradesNum/>}*/}
                </div>
            </div>

        </section>
    );
}

export default ChartShares;