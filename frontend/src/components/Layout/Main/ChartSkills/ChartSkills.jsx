import {useContext, useState} from 'react';
import globalStyles from '../../../../globals.module.css'
import styles from './ChartSkills.module.css';
import SkillsLevel from "./SkillsLevel/SkillsLevel";
import SkillsPoints from "./SkillsPoints/SkillsPoints";
import { TeamContext } from '../../../../context/context'

function ChartSkills() {
    const { isEmployeeId } = useContext(TeamContext);
    const [activeTab, setActiveTab] = useState('skillsLevel');

    return (
        <section id='chartSkills' className={`${globalStyles.chart} ${styles.chartSkills}`}>

            <div className={globalStyles.tabsChart}>
                <div
                    className={`${globalStyles.tabChart} ${activeTab === 'skillsLevel' ? globalStyles.active : ''}`}
                    onClick={() => setActiveTab('skillsLevel')}
                >
                  <p>Уровень владения навыками</p>
                </div>

                <div
                    className={`${globalStyles.tabChart} ${activeTab === 'staffNums' ? globalStyles.active : ''}`}
                    onClick={() => setActiveTab('staffNums')}
                >
                    <p>Баллы сотрудников по навыкам</p>
                </div>
            </div>

            {/* sub-chart content */}
            <div className={globalStyles.tabContentChart}>

                {activeTab === 'skillsLevel'
                    ? <p className={globalStyles.chartSubtitle}>{isEmployeeId ? 'ШКАЛЫ УРОВНЕЙ НАВЫКОВ СОТРУДНИКА' : 'СРЕДНИЕ УРОВНИ НАВЫКОВ КОМАНДЫ'}</p>
                    : ''}

                <div className={globalStyles.scrollableContent}>
                    {activeTab === 'skillsLevel' ? <SkillsLevel/> : <SkillsPoints/>}
                </div>
            </div>

        </section>
    );
}

export default ChartSkills;