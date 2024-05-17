# blog

# Платформа для публикации платного контента
Реализация платформы для публикации записей пользователями. Публикация может быть бесплатной, но неполной, либо платной, для отображения полного текста записи, которая доступна только авторизованному пользователю, который оплатил подписку. Для реализации оплаты подписки используется Stripe. Регистрация пользователя должна быть по номеру телефона.

## Для запуска проекта необходимо:
Клонировать репозиторий.
Создать и активировать виртуальное окружение.
Для работы программы необходимо установить зависимости, указанные в файле requirements.txt.
Создать файл .env, и ввести туда свои настройки как указано в файле .env.sample.

Для запуска проекта с помощью Docker Compose необходимо:

Установить Docker и Docker Compose, если они еще не установлены на вашем компьютере.
Собрать и запустить контейнеры Docker.
Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к проекту.

В проекте выгружены следующие фикстуры:
data_blog.json - данные для создания записей.
data_users.json - данные для создания функционала пользователя.
для загрузки данных фикстур воспользуйтесь командой python manage.py loaddata file_name.json
