import './LayoutDocs.css';

function LayoutDocs() {

    return (
        <section id='charts' className='docs'>
            <div className="column">
                <h2>Документация - Часть 1</h2>
                <p>Текст документации в первом столбце</p>
            </div>
            <div className="column">
                <h2>Документация - Часть 2</h2>
                <p>Текст документации во втором столбце</p>
            </div>

        </section>
    );
}

export default LayoutDocs;