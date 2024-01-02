import re


def coroutine(fun):
    def wrapper(*args,**kwargs):
        gen = fun(*args,**kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def find(chatacter,w):
    while True:
        strings = yield
        list_of_strings = re.findall(r'\w+',strings)
        for string in list_of_strings:
            if string[0] == chatacter:
                w.send(string)

@coroutine
def write(file_name):
    f = open(file_name,'a+')
    while True:
        string = yield
        if string is not None:
            f.write(string + ' ')
            
w = write('res2.txt')
a = find('c',w)
a.send('witam witam  i zo  c ale ma ccccmamsadas cccwasfas ')