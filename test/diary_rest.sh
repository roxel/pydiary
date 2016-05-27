#!/usr/bin/env bash

curl http://127.0.0.1:8333/api/1.0/diary/

POST=$(curl -X POST -H "Content-Type: application/json" -d '{"title":"Dobry dzień", "content": "It was **nice**", "date":"2015-05-25"}' -v http://127.0.0.1:8333/api/1.0/diary/)

curl -v http://127.0.0.1:8333/api/1.0/diary/$POST

curl -X PUT -H "Content-Type: application/json" -d '{"title":"Good day", "content":"It was ***VERY*** **nice**", "date":"2015-05-25"}' -v http://127.0.0.1:8333/api/1.0/diary/$POST

curl -v http://127.0.0.1:8333/api/1.0/diary/$POST

curl -X DELETE -H "Content-Type: application/json" -v http://127.0.0.1:8333/api/1.0/diary/$POST

curl -v http://127.0.0.1:8333/api/1.0/diary/$POST
