import { useContext, useEffect, useState, useCallback } from "react";
import axios from "axios";
import styles from './TopBar.module.css';
import { TeamContext } from "../../../context/context";
import Filter from './Filter/Filter'

function TopBar() {
    const { isTeamTotal, isTeamId, isBusFactor, setBusFactor } = useContext(TeamContext);
    const [isSkillName, setSkillName] = useState("");

    const fetchBusFactor = useCallback(async () => {
        const db_url = `https://dashboard-t5.hopto.org/api/v1/dashboard/bus_factor/?team=${isTeamId}`;
        try {
            let { data } = await axios.get(`${db_url}`, {
                headers: {
                    'Accept': 'application/json',
                },
            });
            setBusFactor(data.bus_factor);
            setSkillName(data.skill);
        } catch (err) {
            console.error(err);
        }
    }, [isTeamId, setBusFactor]);

    useEffect(() => {
        fetchBusFactor();
    }, [fetchBusFactor]);

    return (
        <section id='topbar' className={styles.topBar}>
            {/* 2 small data windows */}
            <section className={styles.wrapData}>
                <div className={styles.innerData}>
                    <div className={styles.innerNum}>{`${isTeamTotal}`}</div>
                    <div className={styles.innerText}>Всего в команде</div>
                </div>

                <div className={`${styles.innerData} ${styles.innerDataBusFactor}`} title={`Навык: ${isSkillName}`}>
                    <div className={styles.innerNum}>{`${isBusFactor}`}</div>
                    <div className={styles.innerText}>Bus-фактор</div>
                </div>
            </section>

            <Filter/>
        </section>
    );
}

export default TopBar;