import functools
def dFact(L):
    def wrapper(fun):
        functools.wraps(fun)
        def inner_wrapper(*args,**kwargs):
            for l in L:
                try:
                    new_args = [arg + l for arg in args]
                    new_kwargs = {key : kwargs[key] + l for key in kwargs}
                    yield fun(*new_args,**new_kwargs)
                except TypeError:
                    return
        return inner_wrapper
    return wrapper 

@dFact([1,2,3,4])
def my_print(*args,**kwargs):
    print(args)
    print(kwargs)
    return 0

a = my_print(1,2,['dasdas'],4,arg = 5,argw = 6)

for element in a:
    print(element)

