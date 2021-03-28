import time


def sleep(func):
    def wrapper():
        time.sleep(10)
        return func()
    return wrapper





wakeup()