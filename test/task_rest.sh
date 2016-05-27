#!/usr/bin/env bash

curl http://127.0.0.1:8333/api/1.0/tasks/

TASK=$(curl -X POST -H "Content-Type: application/json" -d '{"name":"Cleaning2", "done":"true", "date":"2015-02-03", "priority":"0" }' -v http://127.0.0.1:8333/api/1.0/tasks/)

curl -v http://127.0.0.1:8333/api/1.0/tasks/$TASK

curl -X PUT -H "Content-Type: application/json" -d '{"name":"Cleaning2", "done":"true", "date":"2015-02-03", "priority":"-1" }' -v http://127.0.0.1:8333/api/1.0/tasks/$TASK

curl -v http://127.0.0.1:8333/api/1.0/tasks/$TASK

curl -X DELETE -H "Content-Type: application/json" -v http://127.0.0.1:8333/api/1.0/tasks/$TASK

curl -v http://127.0.0.1:8333/api/1.0/tasks/$TASK
