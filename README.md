# API для вычисления коэффициента корреляции Пирсона

Этот проект предоставляет простой API для вычисления коэффициента корреляции Пирсона между двумя наборами данных. Он построен с использованием Django и Django REST Framework и позволяет вводить данные напрямую через JSON или загружать файл Excel.

## Возможности

- Вычисление коэффициента корреляции Пирсона из JSON-данных.
- Вычисление коэффициента корреляции Пирсона из загруженного файла Excel.
- RESTful API дизайн.

### Установка

1. **Клонируйте репозиторий:**

   git clone https://github.com/rutapsz/django-pearson-correlation.git
   cd pearson-correlation-api

2. **Создайте и активируйте виртуальное окружение:**

    python -m venv venv
    source venv\Scripts\activate

3. **Установите необходимые зависимости:**

    pip install -r requirements.txt

4. **Примените миграции:**

    python manage.py migrate

5. **Создайте суперпользователя (опционально):**

    python manage.py createsuperuser

6. **Запустите сервер разработки:**

    python manage.py runserver

### Использование

**Вычисление корреляции из JSON данных:**

Конечная точка: POST /api/pearson/
Заголовки: Content-Type: application/json

Пример запроса:

    curl -X POST http://127.0.0.1:8000/api/pearson/ \
        -H "Content-Type: application/json" \
        -d '{"data1": [1, 2, 3, 4], "data2": [4, 3, 2, 1]}'
Ответ:
    {
    "correlation_coefficient": -1.0
    }

**Вычисление корреляции из файла Excel:**

Конечная точка: POST /api/pearson/
Заголовки: Content-Type: multipart/form-data
Загрузите файл Excel, содержащий два столбца числовых данных.

Пример запроса:

    curl -X POST http://127.0.0.1:8000/api/pearson/ \
        -F "file=@path_to_file.xlsx"
Ответ:

    {
    "correlation_coefficient": <calculated_value>
    }