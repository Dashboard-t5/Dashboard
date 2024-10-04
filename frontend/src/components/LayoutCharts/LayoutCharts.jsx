import './LayoutCharts.css';

function LayoutCharts() {

    return (
        <section id='charts' className='charts'>

            <h1>Чарты</h1>

            <div className="btns">
                <button className="btn btn__data">*</button>
                <button className="btn btn__team">Команда</button>
            </div>

            <p>/* Здесь будут отображаться диаграммы */</p>

        </section>
    );
}

export default LayoutCharts;