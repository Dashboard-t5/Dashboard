# Проект Дашборд📈📊📉 
## _(Хакатон Росбанк, команда №5)_

## _Описание проекта_ 

В проекте представлена реализация аналитического дашборда, разработанного по требованиям заказчика. Дашборд обеспечивает визуализацию текущих навыков сотрудников и их соответствие требованиям должностей. Он позволяет руководителям и HR-специалистам увидеть состояние навыков в командах, сокращает время на анализ показателей команды, позволяет эффективнее планировать развитие и найм сотрудников. Дашборд визуализирует как статические данные на текущий момент, так и динамические данные за период.

![This is an alt text.](https://i.ibb.co/k0N2W8G/2024-10-15-001514.png)


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
git clone git@github.com:Team-number-5-hackathon/Dashboard.git
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

### _Запуск проекта из образов с Docker hub_
1. Для запуска необходимо создать папку проекта, например _dashboard_ и перейти в нее:
```
mkdir dashboard
cd dashboard
```
2. В папку проекта скачиваем файл _docker-compose.production.yml_ и запускаем его:
```
sudo docker compose -f docker-compose.production.yml up
```
Произойдет скачивание образов, создание и включение контейнеров, создание томов и сети.
3. Проверяем доступность проекта по адресу:

https://51.250.40.10

### _Документация к API доступна по адресам:_
https://51.250.40.10/swagger

https://51.250.40.10/api/docs
