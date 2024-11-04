import { Outlet } from 'react-router-dom'
import globalStyles from '../../../globals.module.css'
import styles from './Main.module.css'
import ChartStaff from "./ChartStaff/ChartStaff"
import ChartSkills from "./ChartSkills/ChartSkills"
import ChartShares from "./ChartShares/ChartShares"

function Main() {

    return (
        <main className={`${styles.main} ${globalStyles.section}`}>
            <ChartStaff/>
            <ChartShares/>
            <ChartSkills/>

            <Outlet/>
        </main>
    );
}

export default Main;