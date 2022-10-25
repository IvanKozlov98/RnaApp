# Hospital app
## Описание проекта
1) Пациенты(клиенты) дают больнице свой ДНК.
2) Больница(сервер) уводомляет клиентов о том, если для некоторых из них нашлись родственные связи
3) Больница(сервер) уводомляет клиентов о прибытии новых клиентов той же этнической группы, что и они

## Требования:
- `RabbitMQ` 
- `docker`

## Установка
```sh
pip install -r requirements.txt
```

## Запуск
1) Запуск `rabbitMQ`
```sh
docker-compose up 
```
2) Запуск сервера
```sh
python -m server 
```
3) Запуск клиента
```sh
python -m client 
```
## Использование клиентом
```sh
Enter id: id_person
Enter DNA: dna_person
```
Может прийти сообщения о родственных/этнических связях:
```sh
Relative: Ivan Demid Alex
Ethnic: Ivan Demid Alex Valentine Milan
```
