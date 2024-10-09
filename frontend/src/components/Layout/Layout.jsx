import { Outlet } from 'react-router-dom';
import Sidebar from "./Sidebar/Sidebar"
import Main from "./Main/Main"
import TopBar from "./TopBar/TopBar";
import './Layout.css'

function Layout() {
    return (
        <div className="layout">
            <Sidebar/>
            <TopBar/>
            <Main/>
        </div>
    )
}

export default Layout;