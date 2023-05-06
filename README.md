# Геолокации интересных мест
 
Проект `where_to_go` поможет создать свои сайт с интересными местами поблизости.
Каждому месту можно добавить описание, фотографии и ссылки на официальные ресурсы.
[Посмотреть пример проекта](http://vasadaz.pythonanywhere.com).

Дополнительные возможности:
- load_place загрузку мест в БД  из [JSON-файла](https://github.com/devmanorg/where-to-go-places/tree/master/places)

## Как установить

1. Клонировать репозиторий:

    ```shell
    git clone https://github.com/Vasadaz/where_to_go.git
    ```

2. Установить зависимости:

    ```shell
    pip install -r requirements.txt
    ```

3. Создать файл `.env` с данными:

    ```dotenv
    ALLOWED_HOSTS=secure_host, myhost
    DEBUG=False
    SECRET_KEY=you_secret_key
    ```

4. Применить миграции:

    ```shell
    python3 manage.py migrate
    ```

5. Создать супер-пользователя для доступа к административной панели Django:

    ```shell
    python3 manage.py createsuperuser
    ```

6. Выполнить загрузку мест в БД вручную или из JSON-файла:
   - Для внесения данных вручную выполните команду и перейдите на административную панель Django: 
       ```shell
       python3 manage.py runserver
       ```
   - Для внесения данных с помощью команды подготовьте JSON-файл в формате:
       ```json
       {
       "title": "Заброшенный пионерский лагерь «Белое озеро»",
       "imgs": [
           ...,
           "https://site/media/1.jpg",
           ...,
       ],
       "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
       "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
       "coordinates": {
           "lng": "56.30184799999994",
           "lat": "38.24199999999999"
           }
       }
       ```
       Выполните загрузку файла в БД:
       ```shell 
       python3 manage.py load_place  http://site/places/example.json
       ```
       Изображения сохраняются в `media/images`.
   
   
7. Запуск сайта:
    
    ```shell
    python3 manage.py runserver
    ```
   
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
