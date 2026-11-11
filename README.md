# Learning — примеры интеграций на Python

## Назначение проекта

Набор самостоятельных учебных примеров для практики с сообщениями, сериализацией, кэшем и запросами к БД.

## Функциональность

Отправка и чтение сообщений Kafka и RabbitMQ, примеры Avro со Schema Registry, чтение и обновление товара с Redis-кэшем, выборка пользователей с заказами.

## Архитектура

`kafkaproducer.py`, `kafkaconsumer.py`, `avro*.py` и `rabbit*.py` — отдельные скрипты. `RedisCache.py` и `sqlOptimization.py` содержат FastAPI-роутеры. Compose поднимает Kafka и Schema Registry.

### С чего начать чтение кода

- [`kafkaproducer.py`](kafkaproducer.py)
- [`avroproducer.py`](avroproducer.py)
- [`RedisCache.py`](RedisCache.py)
- [`sqlOptimization.py`](sqlOptimization.py)

[Граф связей Graphify](graphify-out/graph.html) · [Отчёт Graphify](graphify-out/GRAPH_REPORT.md)

Для поиска по графу из корня репозитория выполните `graphify god-nodes --top 5` или `graphify query "имя функции или модуля"`.

## Технологический стек

Python, FastAPI, SQLAlchemy, Redis, Kafka, Confluent Kafka, Avro, Schema Registry, RabbitMQ, Pika, Docker Compose.

## Технические решения

Кэш заполняется после чтения из БД и инвалидируется после обновления. Примеры с брокерами разделяют продюсер и потребитель, чтобы их можно было запускать отдельно.

## Запуск проекта

Поднимите Kafka и Schema Registry командой `docker compose up -d`. Для примера Kafka запустите `python kafkaconsumer.py` в одном терминале и `python kafkaproducer.py` в другом после установки библиотек из импортов. RabbitMQ, Redis и БД для других примеров поднимаются отдельно. TODO — добавить список зависимостей, версию Python и конфигурацию подключений. Общих миграций нет.

## Примеры API

В учебных роутерах есть `GET /products/{product_id}`, `PUT /products/{product_id}` и `GET /users-with-orders`. Перед HTTP-проверкой их нужно подключить к приложению FastAPI и настроить хранилища. Пример команды для Kafka после подготовки окружения.

```bash
python kafkaproducer.py
```

## Тестирование

В исходниках проекта отдельный набор автоматических тестов не обнаружен. Для ручной проверки используйте сценарий из раздела «Примеры API» на тестовой инфраструктуре.

## Ограничения и дальнейшее развитие

Примеры не собраны в единое приложение. Для воспроизводимости нужны настройки подключения и минимальные инструкции по каждому сценарию.

## Мой вклад

TODO — описать свою роль, реализованные компоненты и принятые технические решения.

[Технический обзор проекта](PROJECT_REVIEW.md)
