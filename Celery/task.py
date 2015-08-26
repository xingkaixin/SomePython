from celery import Celery

BROKER_URL = 'sqla+sqlite:///task.db'
BACKEND_URL = 'db+sqlite:///task.db'

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


@app.task
def add(x, y):
    import time
    time.sleep(25)
    return x + y
