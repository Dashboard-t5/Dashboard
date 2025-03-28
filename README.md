# Проект Дашборд📈📊📉 

## _Описание проекта_ 

В проекте представлена реализация аналитического дашборда, разработанного по требованиям заказчика. Дашборд обеспечивает визуализацию текущих навыков сотрудников и их соответствие требованиям должностей. Он позволяет руководителям и HR-специалистам увидеть состояние навыков в командах, сокращает время на анализ показателей команды, позволяет эффективнее планировать развитие и найм сотрудников. Дашборд визуализирует как статические данные на текущий момент, так и динамические данные за период.

![This is an alt text.](https://i.postimg.cc/7brybFyh/2024-10-15-001514.png)


## _Состав команды проекта:_
| Ф.И.О    | Роль в проекте           |    Соц.сеть Telegram                          |
| -----    | -------------------------|-----------------------------------------------|
| Роман    | Продакт-менеджер🎬       |<a href="https://t.me/Trondro">@Trondo</a>     |
| Яна      |Дата-аналитик📉 |<a href="https://t.me/Bogacheva_Yana">@Bogacheva_Yana</a>|
| Андрей   |  Дата-аналитик📈         |<a href="https://t.me/xlegatorx">@xlegatorx</a>|
| Ира      |  Дизайнер  🎨        |<a href="https://t.me/IkraWasHere">@IkraWasHere</a>|
| Анастасия|  Дизайнер🎨    |<a href="https://t.me/anastassiyaa_1">@anastassiyaa_1</a>|
| Павел    | Бизнес-аналитик💼|<a href="https://t.me/Gordeev_Pavel">@Gordeev_Pavel</a>|
| Лара     | Системный аналитик📋     |<a href="https://t.me/Larara">@Larara</a>      |
| Даша     |  Дизайнер 🎨             |<a href="https://t.me/hankarela">@hankarela</a>|
| Владимир|Бэкэнд разработчик👨🏻‍💻|<a href="https://t.me/DziedJanus">@DziedJanus</a>|
| Даша   | Бэкэнд разработчик👩🏻‍💻|<a href="https://t.me/DNFedorova">@DNFedorova</a>|
| Евгений  |Фронтенд разработчик🖼|<a href="https://t.me/EvgenAvdeev">@EvgenAvdeev</a>|



### _Технологии_
* Python 3.11
* Django 4.2
* Django REST Framework
* PostgreSQL
* Nginx
* Gunicorn
* Docker



### _Структура проекта:_

| Имя    | Описание                                                  |
| -----  | --------------------------------------------------------- |
| backend| Файлы для backend разработки                              |
| infra  | Docker-compose файлы для запуска проекта с помощью Docker |

### _Подключенные приложения:_

1. **Employees** - отвечает за характеристики сотрудников.
2. **Ratings** - приложение, связанное с характеристиками и критериями оценок.
3. **Api** - вспомогательное приложение для api.


### _Для запуска проекта локально необходимо:_
1. Клонировать репозиторий и перейти в директорию:

```
git clone git@github.com:Dashboard-t5/Dashboard.git
```

```
cd dashboard/
```

2. Создать и активировать виртуальное окружение:

```
python -m venv venv                      # Устанавливаем виртуальное окружение
source venv/scripts/activate             # Активируем его (Windows); или
source venv/bin/activate                 # Активируем его (Linux)
python -m pip install --upgrade pip      # Обновляем менеджер пакетов pip
pip install -r requirements.txt          # Устанавливаем пакеты для разработки
```
3. Выполнить миграции:
```
python3 manage.py migrate                # для (Linux)
python manage.py migrate                 # для (Windows)
```
4. Загрузить тестовые данные:
```
python3 manage.py import_xlsx

```
5. Создать суперюзера(для входа в админку):
```
python3 manage.py createsuperuser

```
6. Запустить проект локально:
```
python3 manage.py runserver
```
http://localhost:8000/

http://localhost:8000/admin/

http://localhost:8000/swagger/ - документация к API

### _Запуск проекта из образов с Docker hub_
1. Для запуска необходимо создать папку проекта, например _dashboard_ и перейти в нее:
```
mkdir dashboard
cd dashboard
```
2. В дериктории dashboard/ необходимо создать файл _.env_ c переменными окружения. Требуемы переменные приведены в файле _.env_example_

3. В папку проекта скачиваем файлы _docker-compose.prod.yml_ и _nginx.prod.conf_ и запускаем:
```
sudo docker compose -f docker-compose.prod.yml up-d
```
Произойдет скачивание образов, создание и включение контейнеров, создание томов и сети.\
4. Заходим в контейнер backend-a командой:
```
sudo docker compose -f docker-compose.prod.yml exec backend bash
```
Откроется терминал контейнера backend-a в рабочей дериктории.\
5. Собираем файлы статики backend-а в папку:
```
python manage.py collectstatic
```
6. Копируем файлы статики в папку связанную с volume:
```
cp -r /app/collected_static/. /backend_static/static/
```
7. Выполняем миграции командой:
```
python manage.py migrate
```
8. Наполнить базу данных тестовыми данными можно командой:
```
python3 manage.py import_atomic
```
8. Проверяем доступность проекта по адресу:

https://dashboard-t5.hopto.org

### _Документация к API доступна по адресам:_
https://dashboard-t5.hopto.org/swagger

