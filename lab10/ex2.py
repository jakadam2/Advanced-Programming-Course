'''slajd13'''
from typing import Any


class C:

    def __setattr__(self,name,val) -> None:
        if name == 'VarA':
            super().__setattr__(name,val)
            return
        setattr(self.__class__,name,val)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

