# Геолокации интересных мест
 
Проект `where_to_go` поможет создать свои сайт с интересными местами поблизости.
Каждому месту можно добавить описание, фотографии и ссылки на официальные ресурсы.

Дополнительные возможности:
- load_place загрузку мест в БД  из JSON-файла

## Как установить

1. Клонировать репозиторий:

    ```shell
    git clone https://github.com/HardRope/food_bot.git
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

4. Если вы хотите использовать MySQL, тогда:

   - в файл `.env` добавить: 

      ```dotenv
      MYSQL_DB_NAME=mysql_db_name
      MYSQL_USER=mysql_user
      MYSQL_USER_PASSWORD=mysql_user_password
      MYSQL_HOST=mysql_db_host
      MYSQL_PORT=mysql_db_port
      ```

   - в файл `food_bot/settings.py` внести настройки для подключения к MySQL:

       ```python
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'NAME': env.str('MYSQL_DB_NAME'),
               'HOST': env.str('MYSQL_HOST'),
               'PORT': env.str('MYSQL_PORT'),
               'USER': env.str('MYSQL_USER'),
               'PASSWORD': env.str('MYSQL_USER_PASSWORD'),
           }
       }
       ```

5. Сделать миграции:

    ```shell
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

6. Создать супер-пользователя для доступа к административной панели Django:

    ```shell
    python3 manage.py createsuperuser
    ```

7. Выполнить загрузку мест в БД вручную или  из JSON-файла:
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
   
       Если файлов много, то укажите каталог:
       ```shell 
       python3 manage.py load_place  http://site/places
       ```
   
       Все JSON-файлы сохраняются в `static/places`.
       Изображения мест сохраняются в `media/images`.
   
8. Запуск сайта с геолокациями мест:
    
    ```shell
    python3 manage.py runserver
    ```