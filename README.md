# BLOG

## Платформа для публикации платного контента
Реализация платформы для публикации записей пользователями. Публикация может быть бесплатной, но неполной, либо платной, для отображения полного текста записи, которая доступна только авторизованным пользователям, которые оплатили подписку. Для реализации оплаты подписки используется Stripe. Регистрация пользователя должна быть по номеру телефона.

## Стэки:
1. python
2. postgresql
3. django
4. docker

## Для запуска проекта:
1. Клонируйте репозиторий
```bash
  git glone https://github.com/Tatyanalozovaya061/blog.git
```
2. Активируйте виртуальное окружение, установите зависимости
```bash
  python venv\Scripts\activate
```
```bash
  python -m pip install -r requirements.txt 
```
3. Создайте .env файл в корневой директории проекта и заполните следующие переменные:
```bash
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
SECRET_KEY=
STRIPE_SECRET_KEY=
```
5. Выполните миграции
```bash
  python manage.py migrate
```
5. Запустите проект
```bash
    python manage.py runserver
```

## Для запуска докер контейнера:
```bash
  docker compose build
```
```bash
  docker compose up
```
