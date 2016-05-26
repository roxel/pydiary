#!/usr/bin/env bash

curl http://127.0.0.1:8333/api/1.0/tasks/

curl -X POST -H "Content-Type: application/json" -d '{"name":"Cleaning2", "done":"true", "date":"2015-02-03", "priority":"0" }' -v http://127.0.0.1:8333/api/1.0/tasks/