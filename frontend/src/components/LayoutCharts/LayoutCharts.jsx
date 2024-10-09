import './LayoutCharts.css';
import Filter from '../../images/filter.png'
import SearchForm from "./SearchForm/SearchForm"
import ChartStaff from "./ChartStaff/ChartStaff";

function LayoutCharts() {

    return (
        <section id='charts' className='charts'>



            <SearchForm/>

            <ChartStaff/>

        </section>
    );
}

export default LayoutCharts;