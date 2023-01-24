# test_medicine
Тестовый микросервис

### Предусловия для корректной работы микросервиса

* Должен быть установлен python3.8 глобально.


### Установка
#### Как развернуть проект для разработки:

1. Склонируйте проект
```bash
    git clone https://github.com/ArtProPy/test_medicine.git
```

2. Создайте и активируйте виртуальное окружение 

3. Установите poetry
```bash
    pip install poetry
```

4. Установите зависимости проекта
```bash
  poetry install
```

5. Создайте файл `.env` на основе шаблона `.env.template`

6. Накатите миграции:
```bash
  .../venv/bin/django-admin migrate
```

7. Запустите сервер
```bash
  .../venv/bin/django-admin runserver
```

### Ссылки
#### Страница Admin:
```bash
  http://DOMAIN:PORT/admin/
```
#### Страницы Swagger:
```bash
  http://DOMAIN:PORT/doc/
  http://DOMAIN:PORT/redoc/
```
#### Страницы микроссервиса:
```bash
   http://DOMAIN:PORT/refbooks.id/
   http://DOMAIN:PORT/refbooks.name/
   http://DOMAIN:PORT/refbooks/
   http://DOMAIN:PORT/refbooks/<id>/elements.code/
   http://DOMAIN:PORT/refbooks/<id>/elements.value/
   http://DOMAIN:PORT/refbooks/<id>/elements/
   http://DOMAIN:PORT/refbooks/<id>/check_element 
```
