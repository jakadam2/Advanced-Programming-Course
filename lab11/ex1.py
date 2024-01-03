'''slajd6'''
from typing import Any


class MyClass:

    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z
        pass

    def a(self):
        print(f'a: {self.x}')

    def b(self):
        print(f'b: {self.y}')

    def c(self,a):
        print(f'c : {self.z} arg: {a}')


class MyProxy:

    def __init__(self,x,y,z) -> None:
        self._instance = MyClass(x,y,z)

    def __getattribute__(self, __name: str) -> Any:
        instance = super().__getattribute__('_instance')
        return getattr(instance,__name)


    
