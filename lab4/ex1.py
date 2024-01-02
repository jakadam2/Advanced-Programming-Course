class MyPair:

    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        pass

    def __eq__(self, key) -> bool:
        print(type(key))
        return key == self.key if type(key) is not MyPair.__class__ else key.key == self.key and key.value == self.value


class MyDict:

    def __init__(self) -> None:
        self.cont:MyPair = []
        pass

    def __getitem__(self,key):
        for pair in self.cont:
            if pair.key == key:
                return pair.value
        raise KeyError(key)
    
    def __setitem__(self,key,value):
        for pair in self.cont:
            if pair.key == key:
                pair.value = value
                return
        self.cont.append(MyPair(key,value))

    def __contains__(self,key):
        return key in self.cont
    
    def __eq__(self,another_MyDict) -> bool:
        return self.cont == another_MyDict.cont
    

