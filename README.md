### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd kittygram2plus
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить веб-сервер:

```
python manage.py runserver
```
создайте через API несколько пользователей:
````
отправьте POST-запрос на http://127.0.0.1:8000/auth/users/, передав их в полях username и password.
{
    "username": "user1",
    "password": "password1"
}
``````
отправьте POST-запрос на эндпоинт /auth/jwt/create/, передав действующий логин и пароль в полях username и password.
API вернёт JWT-токен в поле access.можно выбрать соответствующий тип авторизации во вкладке Authorization и указать JWT-токен
`````
добавьте котиков в базу
`````
Чтобы создать в БД первую запись с котиком, выполните POST-запрос к проекту /cats/ и передайте поля name, color и birth_year, owner, achievements в полях.
{
    "name": "Сяська",
    "color": "Mixed",
    "birth_year": "2020",
    "owner": "user1",
    "achievements": [
        {"achievement_name": "лежать"},
        {"achievement_name": "кусать всех"}
    ]
}
`````

