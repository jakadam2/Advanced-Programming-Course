def decor(obj):
    old_init = obj.__init__
    def new_init(self,*args,**kwargs):
        self._args = args
        self._kwargs = kwargs
    def give_arguments(self):
        return (self._args,self._kwargs)
    obj.__init__ = new_init
    obj.give_arguments = give_arguments
    return obj

@decor
class Test:
    def __init__(self,*args,**kwargs) -> None:
        pass

a = Test(1,2,3,4,a = 412412)
b = Test(3,3,33)

print(a.give_arguments())
print(b.give_arguments())