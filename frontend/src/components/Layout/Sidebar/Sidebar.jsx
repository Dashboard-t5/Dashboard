import {NavLink} from 'react-router-dom'
import './Sidebar.css'
import BtnEmpty from '../../../images/btn_empty.png'
import Men from '../../../images/btn_users.png'
import {useState} from "react";

function Sidebar() {
    const [activeBtn, setActiveBtn] = useState('men')

    return (
        <nav id='sidebar' className='sidebar'>

            <aside className="sidebar__inner-bar">
                <ul className="inner__half">
                    <li className="btn__wrap">
                        <img src={BtnEmpty} className="inner__icon-bg" alt="btn empty"/>
                    </li>
                    <li className="btn__wrap">
                        <img src={BtnEmpty} className="inner__icon-bg" alt={"btn empty"}/>
                    </li>
                    <li className={`btn__wrap ${activeBtn==='men' ? 'active' : ''}`} >
                        <NavLink to="/" end onClick={() => setActiveBtn('men')}>
                            <img src={Men} className="inner__icon-bg" alt={"men"}/>
                        </NavLink>
                    </li>
                </ul>
                <ul className="inner__half"></ul>
            </aside>

        </nav>
    );
}

export default Sidebar;
