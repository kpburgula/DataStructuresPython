from celery import Celery
import time
app = Celery('tasks', broker='amqp://localhost')
@app.task
def some_func(something):
	time.sleep(5)
	return str(something)

# celery -A tasks worker --loglevel=info --concurrency=1

