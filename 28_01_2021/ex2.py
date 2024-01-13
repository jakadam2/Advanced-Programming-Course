def check_args(amount):
    def wrapper(fun):
        def inner_wrapper(*args,**kwargs):
            if len(args) + len(kwargs) != amount:
                raise TypeError
            else:
                return fun(*args,**kwargs)
        return inner_wrapper
    return wrapper

        