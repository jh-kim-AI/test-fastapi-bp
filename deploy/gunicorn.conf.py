# Listen to the internal network port
bind = '0.0.0.0:8001'

# Work list
chdir = '/nebula/app'

# Number of parallel worker processes
workers = 1

# Specify the number of threads per worker
threads = 4

# Listen to the queue
backlog = 512

# Overtime time
timeout = 120

# Set up the deamon process and hand over the process to supervisor management;
# if set to True, the supervisor startup log is:
# Gave up: nebula_server entered FATAL state, too many start retries too quickly
# then you need to change this to: False
daemon = True

# Work mode coroutine
worker_class = 'uvicorn.workers.UvicornWorker'

# Set process file directory
pidfile = '/nebula/gunicorn.pid'

# Set access log and error information log paths
accesslog = '/var/log/nebula_server/gunicorn_access.log'
errorlog = '/var/log/nebula_server/gunicorn_error.log'

# Set this value to true to record the printing information in the error log
capture_output = True

# Set logging level
loglevel = 'debug'

# Python program
pythonpath='/usr/local/bin/python3.11/site-packages'

# Start gunicorn -c gunicorn.conf.py main:app
