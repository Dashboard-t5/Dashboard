import { useState } from 'react';
import { useLocation } from 'react-router-dom';
<<<<<<< HEAD
import styles from './SearchForm.module.css';
=======
import styles from './SearchForm.module.css'; // Импортируем стили как модуль
>>>>>>> front-dev
import { useLocalStorageState as useStorage } from '../../../hooks/useLocalStorageState';

function SearchForm() {
    const location = useLocation();

    const [isPlaceholder, setPlaceholder] = useState('Введите запрос');
    const [isSearchWord, setSearchWord] = useStorage('searchWord', ''); // key = 'searchWord', '' = initial value

    function handleInput(evt) {
<<<<<<< HEAD
        if (evt && evt.target && location.pathname === '/') {
            localStorage.setItem('searchWord', JSON.stringify(evt.target.value));
=======
        if (location.pathname === '/') {
            localStorage.setItem('searchWord', JSON.stringify(evt.target.value)); // сохраняем искомое слово в ЛС
>>>>>>> front-dev
            setSearchWord(evt.target.value);
        }
    }

    function handleSubmitSearch(evt) {
        evt.preventDefault();
        if (location.pathname === '/') {
<<<<<<< HEAD
            const searchWord = JSON.parse(localStorage.getItem('searchWord'));
=======
            const searchWord = JSON.parse(localStorage.getItem('searchWord')); // достаем 'searchWord' из ЛС
>>>>>>> front-dev
            // можно добавить логику для поиска
        } else {
            setPlaceholder('Введите запрос');
        }
    }

    return (
        <form onSubmit={handleSubmitSearch} className={`${styles.searchForm}`} id="search" name="search">
            <div className={styles.searchWrap}>
                <button type="submit" className={`${styles.searchLoupeBtn} ${styles.searchLoupeImg}`}></button>
                <input
                    type="text"
<<<<<<< HEAD
                    value={isSearchWord || ''}
=======
                    value={isSearchWord ? isSearchWord : ''}
>>>>>>> front-dev
                    className={styles.searchInput}
                    id="search-input"
                    name="search"
                    placeholder={isPlaceholder}
                    onChange={handleInput}
                />
            </div>
        </form>
    );
}

export default SearchForm;