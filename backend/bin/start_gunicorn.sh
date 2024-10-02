#!/bin/bash

source /home/QuEZ/env/bin/activate
cd /home/QuEZ/backend/src/
exec gunicorn -c /home/QuEZ/backend/gunicorn_config.py -k uvicorn.workers.UvicornWorker main:app
