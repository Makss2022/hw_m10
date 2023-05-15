1.  Открыть в терминале папку ~/quotes, в корне которой лежат файлы 'Dockerfile'
    и 'docker-compose.yml', и запустить команду 'docker-compose up -d';

2.  Затем запустить клманду 'docker-compose exec web python manage.py migrate'
    для применения начальной миграци;

3.  Запустить клманду 'docker-compose exec web python -m utils.migration' - эта
    команда запускает утилиту для выполнения миграции базы данных с MongoDB,
    которая существует в облачном хранилище MongoDB Atlas
    (https://www.mongodb.com/cloud/atlas), в Postgres для нашего сайта;

        Теперь можно запустить сайт в браузире по адрусу http://localhost:8000/ или
        http://127.0.0.1:8000/


        Чтобы пользоваться административной панелью Django запустите команду

    'docker-compose exec web python manage.py createsuperuser'. Затем введите
    имя пользователя, его email и пароль. Если пароль будет слишком простым то
    будет задан дополнительный вопрос, уверены ли мы, отвечаем да.

После того как пользователь успешно создан, вы можете зайти на
http://localhost:8000/admin/ или http://127.0.0.1:8000/admin/, используя имя и
пароль для нового пользователя
