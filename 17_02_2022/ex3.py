class Test:
    def __init__(self) -> None:
        pass
        
    def a(self):
        print('a')

    def b(self):
        print('b')

    def c(self):
        print('c')


class ProtectingClass:
    def __init__(self,protected_class) -> None:
        self.__insatnce = protected_class

    def __getattr__(self,name):
        if name not in ['a','b']:
            raise AttributeError('WRONG METHOD!!!')
        else:
            return getattr(self.__insatnce,name)
        