from copy import deepcopy

class C:

    d = 6
    e = 'asas'
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def addProperty(cls):
        for key in vars(cls):
            if not key.startswith('__') and type(getattr(cls,key)) is str:
                setattr(cls,key,getattr(cls,key))

                def getter(cls):
                    return getattr(cls,deepcopy('__' + key))
                def setter(cls,value):
                    if type(value) is str:
                        cls.__dict__[key] = value
                    else:
                        raise TypeError()
                setattr(cls,key,property(getter,setter))

a = C(1,2,'sfafas')
a.addProperty()
print(a.e)