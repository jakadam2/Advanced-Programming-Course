'''slajd6nizej'''
def swap_methods(ff,fun):
    def decorator(obj):
        def new_getattribute(self,name):
            if name == fun:
                return object.__getattribute__(self,ff)
            return object.__getattribute__(self,name)
        obj.__getattribute__ = new_getattribute
        return obj
    return decorator
    
@swap_methods('b','a')
class Test:

    def b(self):
        print('b')

