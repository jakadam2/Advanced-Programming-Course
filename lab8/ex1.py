import functools
'''21slajd'''
def decf(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        if len(args) + len(kwargs) != 2:
            raise TypeError(len(args) + len(kwargs))
        result = function(*args,**kwargs)
        with open('result.txt','a+') as f:
            f.write(str(result + int(args[0])))
        return result
    return wrapper

