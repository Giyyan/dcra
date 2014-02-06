# coding=utf-8
from celery import Celery
from pprint import pformat
from celery.events.snapshot import Polaroid

from celery import Celery


def my_monitor(app):
    state = app.events.State()

    def on_event(event):
        print "EVENT HAPPENED: ", event

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                '*': on_event,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)

if __name__ == '__main__':
    app = Celery(broker='amqp://guest@localhost//')
    my_monitor(app)