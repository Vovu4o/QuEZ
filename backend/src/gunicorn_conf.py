from multiprocessing import cpu_count

bind = 'unix:/home/QuEZ/backend/src/gunicorn.sock'

 # Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/QuEZ/backend/src/access_log'
errorlog =  '/home/QuEZ/backend/src/error_log'
