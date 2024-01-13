import functools
import re

def coroutine(fun):
    functools.wraps(fun)
    def wrapper(*args,**kwargs):
        gen = fun(*args,**kwargs)
        next(gen)
        return gen
    return wrapper


@coroutine
def listCreator(stop):
    my_list = []
    while True:
        element = (yield)
        my_list.append(element)
        print(f'Actual list: {my_list}')


@coroutine
def searcher(c1,c2,receiver1,receiver2):
    while True:
        file_name = (yield)
        try:
            with open(file_name) as f:
                words = f.read()
                words = re.split('\n| ', words)
                for word in words:
                    if word.startswith(c1):
                        receiver1.send(word)
                    if word.startswith(c2):
                        receiver2.send(word)

        except FileNotFoundError:
            print(f'File {file_name} does not exist')

a = searcher(1,1,1,1)
a.send('dasdasdasdasd')
a.send('test.txt')