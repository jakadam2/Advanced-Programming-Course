import functools
'''slajd23'''
def decora(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        for arg in args:
            if type(arg) != str:
                raise TypeError()
        for key in kwargs:
            if type(kwargs[key]) != str:
                raise TypeError()
        result = function(*args,**kwargs)
        result_string = ''
        for arg in args:
            result_string += f'{arg} '
        for key in kwargs:
            result_string += f'{kwargs[key]} '   
        result_string += str(result)
        return result_string
    return wrapper  