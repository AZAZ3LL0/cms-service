from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/gumaonelove/besm/cms_service/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'