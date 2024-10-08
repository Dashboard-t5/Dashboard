import { useState } from 'react'
import './ChartStaff.css'
import LayoutSkills from './LayoutSkills/LayoutSkills'
import LayoutStaffNums from './LayoutStaffNums/LayoutStaffNums'

function ChartStaff() {
    const [activeTab, setActiveTab] = useState('skillsLevel')

    return (
        <section id='chartStaff' className='chartStaff'>

            <div className="tabs-chart">
                <div className={`tab-chart ${activeTab === 'skillsLevel' ? 'active' : ''}`}
                     onClick={() => setActiveTab('skillsLevel')}>
                    <p>Соответствие должности</p>
                    {/*<span>Сотрудник: _ • Уровень владения навыками</span>*/}
                </div>

                <div className={`tab-chart ${activeTab === 'staffNums' ? 'active' : ''}`}
                        onClick={() => setActiveTab('staffNums')}>
                    Количество сотрудников, владеющих навыками
                </div>
            </div>

            <div className="tab-content-chart">
                {activeTab === 'skillsLevel' ? <LayoutSkills/> : <LayoutStaffNums/>}
            </div>


        </section>
    );
}

export default ChartStaff;