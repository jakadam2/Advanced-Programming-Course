class MyTuple(tuple):
    def __new__(cls,iter):
        return super().__new__(cls,[iter[i] for i in range(1,len(iter),2)])