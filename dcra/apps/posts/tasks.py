import random
from celery import shared_task
from time import sleep


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    sleep(60 * random.random())
    result = x * y

    return result


@shared_task
def xsum(numbers):
    return sum(numbers)