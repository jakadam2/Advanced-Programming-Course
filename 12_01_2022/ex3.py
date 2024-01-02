from typing import Any


class C:
    def __init__(self) -> None:
        self.VarA = None
        pass
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name != 'VarA' and __name != 'VarB':
            setattr(self.__class__,__name,__value)
        else:
            self.__dict__[__name] = __value

    def __getatte__(self,__name):
        if __name != 'VarA' and __name != 'VarB':
            return getattr(self.__class__,__name)
        else:
            return getattr(self,__name)
    
a = C()
b = C()
a.a = 6
print(b.a)
a.VarA = 3
print(b.VarA)