import functools

def coroutine(fun):
    functools.wraps(fun)
    def wrapper(*args,**kwargs):
        gen = fun(*args,**kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def handler0_100(suc = None):
    while True:
        event = (yield)
        if 0 <= event <= 100:
            print(f'Event {event} is proced by handler0_100')
        elif suc is not None:
            try:
                suc.send(event)
            except StopIteration:
                return

@coroutine
def handler100_200(suc = None):
    while True:
        event = (yield)
        if 100 <= event <= 200:
            print(f'Event {event} is proced by handler100_200')
        elif suc is not None:
            try:
                suc.send(event)
            except StopIteration:
                return

@coroutine
def negative_handler(suc = None):
    while True:
        event = (yield)
        if event < 0:
            print(f'Event {event} is proced by negative_handler')
            return
        elif suc is not None:
            suc.send(event)

@coroutine
def defalut_handler(suc = None):
    while True:
        event = (yield)
        print(f'Event {event} is proced by default_handler')

