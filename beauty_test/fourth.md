Система очистки может быть следующей:

1. Создаём TTL индекс.
2. Добавляем поле TTL-индекса к нужным документам.

Пример может выглядеть так:

```
db.log_events.createIndex( { "createdAt": 1 }, { expireAfterSeconds: 86400 } )

db.log_events.insertOne( {
   "createdAt": new Date(),
   "logEvent": 2,
   "logMessage": "Success!"
} )
```
Данный документ автоматически исчезнет спустя 24 часа.
