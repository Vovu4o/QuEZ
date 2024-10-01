#!/bin/bash

NAME=fastapi-app
DIR=/home/QuEZ
USER=root
WORKERS=3
WORKER_CLASS=uvicorn.workers.UvicornWorker
VENV=$DIR/env/bin/activate
BIND=unix:$DIR/backend/src/gunicorn.sock
LOG_LEVEL=error

cd $DIR
source $VENV

exec gunicorn main:app \
  --name $NAME \
  --workers $WORKERS \
  --worker-class $WORKER_CLASS \
  --user=$USER \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-
