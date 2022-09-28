### О проекте:

Данный проект является классическим примером отзовика с возможностями API.
В качестве фреймворка использовался Django 2.2.16.
Дополнительно использовались следующие пакеты: Django-filter 22.1, Django REST framework 3.12.4, Simple JWT 4.7.2.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Inozem/infra_sp2.git
cd infra_sp2/infra/
```

Создать файл .env и добавить в него переменные с нужными значениями:
DB_ENGINE
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT
SECRET_KEY

```
echo $null >> ./.env
.env
```

Cобрать контейнер:

```
docker-compose up -d --build
```

Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Собрать статику:

```
docker-compose exec web python manage.py collectstatic --no-input 
```

Заполнить базу данных тестовыми данными:

```
docker-compose exec web python manage.py install_bd
```


### Информация:

Регистрация:
Регистрация происходит путем отправки POST запроса с указание пользовательского имени и адреса электронной почты.

Пример запроса регистрации нового пользрвателя:
```
POST http://localhost/api/v1/auth/signup/
Content-Type: application/json

{
    "username": "1112",
    "email": "1112@qwe.ru"
}
```

Пример ответа:
```
{
  "email": "1112@qwe.ru",
  "username": "1112"
}
```

После успешной регистрации на почту придет секретный код, который позволит подтвердить почту и получить токен аутентификации.
Пример секретного кода: MSBrKI8ZkD


Подтверждение адреса электронной почты и получение токена аутентификации:

Пример запроса:
```
POST http://localhost/api/v1/auth/signup/
Content-Type: application/json

{
    "username": "1112",
    "confirmation_code": "MSBrKI8ZkD"
}
```

Пример ответа:
```
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NjEyMzg1LCJqdGkiOiJiNjI4N2Y3Y2JhMGQ0ZThjOGM3NGM2MTcwMDI4NjdkMCIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiMTExMiIsImNvbmZpcm1hdGlvbl9jb2RlIjoiTVNCcktJOFprRCJ9.5wo80prs8WWwIZrsESG-fL9xl0jfNSYVq5mdFdpIVxs"
}
```

Подробнее с примерами запросов можно ознакомиться по ссылке http://localhost/redoc/ .

Авторы проекта: Иноземцев Сергей и Недря Сергей


![CI](https://github.com/Inozem/yamdb_final/actions/workflows/main.yml/badge.svg?branch=master)
