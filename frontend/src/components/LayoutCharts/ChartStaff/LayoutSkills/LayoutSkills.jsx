import './LayoutSkills.css'
function LayoutSkills() {
    return (
        <div>
            <p className='chart__subtitle'>Сотрудник: ${}_ • Уровень владения навыками</p>
            <table className='chart__table'>
                <tr>
                    <th className='table__header'>Сотрудник</th>
                    <th>Доля навыков с удовлетворительной оценкой</th>
                </tr>
                <tr>
                    <td>Ефремовв Вячеславв</td>
                    <td>79%%</td>
                </tr>

            </table>

        </div>
    )
}

export default LayoutSkills