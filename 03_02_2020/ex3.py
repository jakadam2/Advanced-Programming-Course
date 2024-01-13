class BaseClass:
    def m(cls):
        print('i am from base class')


def MakeBase(obj):
	class new_class(obj,BaseClass):
		pass
	return new_class


class Test:
    def __init__(self) -> None:
          pass


a = Test()
Test.m()
