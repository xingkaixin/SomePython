from celery import Celery
import time

BROKER_URL = 'sqla+sqlite:///task.db'
BACKEND_URL = 'db+sqlite:///task.db'

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

"""
celery -A task worker -P gevent --loglevel=info
"""


@app.task
def add(x, y):
    time.sleep(1)
    return x + y


@app.task
def minus(x, y):
    i = 0
    while i < 50:
        time.sleep(1)
        print x - y
        i += 10
    return x - y
