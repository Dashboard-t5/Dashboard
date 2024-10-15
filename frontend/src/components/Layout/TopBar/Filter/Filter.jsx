import FilterIcon from "../../../../images/filter.png";
import { TeamContext } from "../../../../context/context";
import {useContext, useEffect, useState} from "react";
import axios from "axios";
import styles from './Filter.module.css'

function Filter() {
    const { isTeamId } = useContext(TeamContext);
    const [isTeamName, setTeamName] = useState("");

    useEffect(() => {
        getTeamNames();
    }, [isTeamId]);

    const getTeamNames = async () => {
        const db_url = `https://dashboard-t5.hopto.org/api/v1/teams`;
        try {
            let { data } = await axios.get(`${db_url}`, {
                headers: {
                    'Accept': 'application/json',
                },
            });
            console.log(data)
            setTeamName(data)
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div className={styles.filterWrap}>
            <img src={FilterIcon} className={styles.chartsFilter} alt={'filter'}/>
        </div>
    );
}

export default Filter;