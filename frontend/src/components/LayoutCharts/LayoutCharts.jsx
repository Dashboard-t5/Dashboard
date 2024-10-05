import './LayoutCharts.css';
import Filter from '../../images/filter.png'
import SearchForm from "../SearchForm/SearchForm"

function LayoutCharts() {

    return (
        <section id='charts' className='charts'>

            <div className="btns">
                <button className="btn btn__data">-</button>
                <button className="btn btn__team">Команда</button>
                <img src={Filter} className="charts_filter" alt={'filter'}/>
            </div>

            {/* 2 small data windows */}
            <section className="wrap-data">
                <div className="inner-data">
                    <div className="inner inner_num">0</div>
                    <div className="inner inner_text">Всего в команде</div>
                </div>

                <div className="inner-data">
                    <div className="inner inner_num">0</div>
                    <div className="inner inner_text">Bus-фактор</div>
                </div>
            </section>

            <SearchForm/>

        </section>
    );
}

export default LayoutCharts;