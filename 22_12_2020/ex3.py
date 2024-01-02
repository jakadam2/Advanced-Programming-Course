def fabDecor(t):
    def wrapper(obj):
        @staticmethod
        def inner_wrapper():
            subclasses = obj.__mro__
            for subclass in subclasses:
                for key in vars(subclass):
                    if not callable(getattr(subclass,key)) and not key.startswith('__') and type(getattr(subclass,key)) == t:
                        yield ((key,subclass.__name__,getattr(subclass,key)))
        
        setattr(obj,'checkTypes',inner_wrapper)
        return obj
    return wrapper



class NadNadTest:
    e = 10

class NadTest(NadNadTest):
    d = 5

@fabDecor(int)
class Test(NadTest):
    a = 1
    def __init__(self) -> None:
        self.c = 4
    
def a():
    for i in range(8):
        print(i)

def b():
    return a

a = Test()
b = a.checkTypes()
for c in b:
    print(c)