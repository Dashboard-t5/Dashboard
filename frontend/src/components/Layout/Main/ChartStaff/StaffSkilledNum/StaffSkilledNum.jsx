import styles from './StaffSkilledNum.module.css';
<<<<<<< HEAD

function StaffSkilledNum() {
=======
import { useState } from 'react';

function StaffSkilledNum() {
    const [isActiveBtn, setActiveBtn] = useState('hardSkill');
>>>>>>> front-dev

    return (
        <div>
            <span className={styles.chartBtnsWrap}>
<<<<<<< HEAD
=======
                <button
                    onClick={() => setActiveBtn('hardSkill')}
                    className={`${styles.chartBtn} ${styles.chartBtnHSkill} ${isActiveBtn === 'hardSkill' ? styles.chartBtnActive : ''}`}
                >
                    Hard Skill
                </button>
                <button
                    onClick={() => setActiveBtn('softSkill')}
                    className={`${styles.chartBtn} ${isActiveBtn === 'softSkill' ? styles.chartBtnActive : ''}`}
                >
                    Soft Skill
                </button>
>>>>>>> front-dev
            </span>

            <p className={styles.chartSubtitle}>Сотрудник •</p>
        </div>
    );
}

export default StaffSkilledNum;