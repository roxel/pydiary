#!/usr/bin/env bash

curl http://127.0.0.1:8333/api/1.0/tasks/

curl http://127.0.0.1:8333/api/1.0/tasks/ -d "name=Cleaning&date=2016-05-04&priority=0&done=n" -X POST -v
