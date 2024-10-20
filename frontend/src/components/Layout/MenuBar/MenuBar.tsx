import { useContext, useEffect, useState, useCallback } from "react";
import axios from "axios";
import globalStyles from '../../../globals.module.css'
import styles from './MenuBar.module.css';
import { TeamContext } from "../../../context/context";
import Filter from './Filter/Filter';

interface BusFactorResponse {
    bus_factor: number;
    skill: string;
}

function MenuBar() {
    const { isTeamTotal, isTeamId, isBusFactor, setBusFactor } = useContext(TeamContext);
    const [isSkillName, setSkillName] = useState<string>("");

    const getBusFactor = useCallback(async () => {
        const db_url = `https://dashboard-t5.hopto.org/api/v1/dashboard/bus_factor/?team=${isTeamId}`;
        try {
            const { data } = await axios.get<BusFactorResponse>(`${db_url}`, {
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
        getBusFactor();
    }, [getBusFactor]);

    return (
        <section id="menubar" className={`${styles.menuBar} ${globalStyles.section}`}>
            {/* 2 small data windows */}
            <section className={styles.wrapData}>
                <div className={styles.innerData}>
                    <div className={styles.innerNum}>{isTeamTotal}</div>
                    <div className={styles.innerText}>Всего в команде</div>
                </div>

                <div className={`${styles.innerData} ${styles.innerDataBusFactor}`} title={`Навык: ${isSkillName}`}>
                    <div className={styles.innerNum}>{isBusFactor}</div>
                    <div className={styles.innerText}>Bus-фактор</div>
                </div>
            </section>

            <Filter />
        </section>
    );
}

export default MenuBar;