# Dashboard

Дашборд аналитики по навыкам сотрудников позволяет руководителю увидеть состояние навыков в командах, сокращает время на анализ показателей команды, позволяет эффективнее планировать развитие и найм сотрудников.
### Технологии
* Python
* Django
* Django REST Framework
* PostgreSQL

#### Для локальной разработки нужно:
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
## Ветки! 

- main - это продакт ветка. Из push-а в эту ветку будем планировать делать workflow
- dev - это ветка текущей разработки. Берем новую задачу, под нее создаём новую ветку. Называем её
    lasouski_users_app. Пушим её на github и делаем pullrequest в эту ветку dev. Отмечаем кто должен
    сделать review.
