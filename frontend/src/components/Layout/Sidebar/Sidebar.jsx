import {NavLink} from 'react-router-dom'
import './Sidebar.css'
import BtnCirclesFour from '../../../images/btn_circles_four.png'
import BtnEmpty from '../../../images/btn_empty.png'
import Men from '../../../images/btn_men.png'

function Sidebar() {

    return (
        <nav id='sidebar' className='sidebar'>

            <aside className="sidebar__inner-bar">
                <div className="inner__half">
                    <img src={BtnEmpty} className="inner__icon" alt={"btn empty"}/>
                    <img src={BtnEmpty} className="inner__icon" alt={"btn empty"}/>
                    <NavLink to="/" end><img src={Men} className="inner__icon" alt={"men"}/></NavLink>
                </div>
                <div className="inner__half"></div>
            </aside>

        </nav>
    );
}

export default Sidebar;
