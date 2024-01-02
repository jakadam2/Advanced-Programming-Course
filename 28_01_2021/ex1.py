def coroutine(func):
    @functools.wrap(func)
    def wrapper(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return wrapper
@coroutine
def ag_handler(succesor = None):
    try:
        while True:
            word = yield
            if word[0] >= 'a' and word[0] <= 'g':
                print('event ',word,' is directed by ag_handler')
            elif succesor is not None:
                succesor.send(word)
    except:
        print('My succesor:', succesor)
@coroutine
def hn_handler(succesor = None):
    while True:
        word = yield
        if word[0] >= 'h' and word[0] <= 'n':
            print('event ',word,' is directed by hn_handler')
        elif succesor is not None:
            succesor.send(word)   
@coroutine
def non_letter_handler(succesor = None):
    while True:
        word = yield
        if word[0] < 'a' and word[0] > 'z':
            print('event ',word,' is directed by non_letter_handler')
        elif succesor is not None:
            succesor.send(word)
@coroutine
def default_handler():
    while True:
        word = yield
        print('event ',word,' is directed by default_handler')

pipeline = ag_handler(hn_handler(non_letter_handler(default_handler())))
pipeline.send('aadgsdgdg')