'''slajd7'''
import functools

def coroutine(fun):
    functools.wraps(fun)
    def wrapper(*args,**kwargs):
        gen = fun(*args,**kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def handler04(suc = None):
    while True:
        event = (yield)
        if 0 <= event[0] <= 4 and isinstance(event,list):
            print(f'Event {event} handler04')
        elif suc is not None:
            suc.send(event)

@coroutine
def handler59(suc = None):
    while True:
        event = (yield)
        if 5 <= event[0] <= 9 and isinstance(event,list):
            print(f'Event {event} handler59')
        elif suc is not None:
            suc.send(event)

@coroutine
def handlergt9(suc = None):
      while True:
        event = (yield)
        if event[0] < 9 and isinstance(event,list):
            print(f'Event {event} handlergt9 I will modify event')
        elif suc is not None:
            suc.send(event[0] - event[1])

@coroutine
def default_handler(suc = None):
      while True:
        event = (yield)
        if event < 9 and isinstance(event,list):
            print(f'Event {event} default')

pipeline = handler04(handler59(handlergt9(default_handler())))


