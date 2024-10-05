import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import LayoutCharts from '../LayoutCharts/LayoutCharts'
import LayoutDocs from '../LayoutDocs/LayoutDocs'
import './Main.css'

function Main({ type }) {
    const [activeTab, setActiveTab] = useState('charts')

    return (
        <main className="main">
            <div className="tabs">

                <button className={`tab ${activeTab==='charts' ? 'active' : ''}`}
                        onClick={() => setActiveTab('charts')}>
                    Чарты
                </button>
                <button className={`tab ${activeTab==='docs' ? 'active' : ''}`}
                        onClick={() => setActiveTab('docs')}>
                    Документация
                </button>
            </div>

            <div className="tab-content">
                {activeTab === 'charts' ? <LayoutCharts/> : <LayoutDocs/>}
            </div>

            <Outlet/>

        </main>
    );
}

export default Main;