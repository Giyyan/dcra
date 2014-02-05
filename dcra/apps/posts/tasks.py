from celery import shared_task
from celery.task import periodic_task
from datetime import timedelta
from time import sleep


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    sleep(60)
    result = x * y

    return result


@shared_task
def xsum(numbers):
    return sum(numbers)