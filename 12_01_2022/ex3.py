from typing import Any


class C:

    __slots__ = ['VarA','VarB']

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'VarA' or __name == 'VarB':
            super().__setattr__(__name,__value)
        else:
            setattr(self.__class__,__name,__value)

