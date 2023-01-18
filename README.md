## API Yatube

Проект представляет собой API приложение для сайта-блога Yatube

Весь функционал сайта реализован с помощью api

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:maxsause/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API
Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.
```
GET /api/v1/posts/
```
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
```
POST /api/v1/posts/
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
По адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) доступна документация ко всем запросам к API
