def dFact(list_shift):
    def wrapper(fun):
        def inner_wrapper(*args,**kwargs):
            for shift in list_shift:
                new_args = [arg + shift for arg in args]
                new_kwagrs = {key:arg + shift for key,arg in kwargs.items()}
                try:
                    res = fun(*new_args,**new_kwagrs)
                except:
                    return StopIteration
                yield res
        return inner_wrapper
    return wrapper

@dFact([1,2,3,4])
def p(number):
    print(number)
    return number

for a in p(1):
    print(a)