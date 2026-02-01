# Запуск проекта через Docker Compose

## Требования
- Установленный [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/)

## Шаги по запуску

1. Скопируйте шаблон переменных окружения:
   ```bash
   cp .env.example .env
2. Откройте файл .env и убедитесь, что все переменные заполнены корректно. Особенно обратите внимание на:
- SECRET_KEY — должен быть уникальным (можно сгенерировать через Django)
- DB_PASSWORD — пароль от базы данных
- STRIPE_SECRET_KEY — если используется Stripe

## Запуск проекта
3. Запустите все сервисы одной командой:
   ```bash
   docker compose up --build
   
4. Дождитесь завершения миграций. В логах вы увидите сообщение:
   ```text
   Starting development server at http://0.0.0.0:8000/
   
## Проверка работоспособности сервисов
- Бэкенд (Django API)
Откройте в браузере:
→ http://localhost:8000/swagger/
Должна открыться интерактивная документация API.
- PostgreSQL (база данных)
Выполните в терминале:
   ```bash
   docker compose exec db psql -U postgres -c "SELECT version();"
 Ожидаемый результат — строка с версией PostgreSQL.

- Redis (брокер сообщений)
Выполните:
   ```bash
   docker compose exec redis redis-cli PING
Ожидаемый ответ: PONG.
 
- Celery Worker (фоновые задачи)
Выполните:
  ```bash
   docker compose logs celery_worker | grep "ready"

В выводе должно быть: celery@... ready.

- Celery Beat (периодические задачи)
Выполните:
   ```bash
   docker compose logs celery_beat  
