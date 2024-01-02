class C:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def m0(self,a1,a2):
        return 'm0'
    
    def m1(self,b1,b2,b3,b4,b5):
        return 'm1'
    
def apply(to_do):
    result = []
    obj = to_do[0][0](*to_do[0][1:])
    result.append(obj)
    for command in to_do[1:]:
        result.append(getattr(obj,command[0])(*command[1:]))
    return result

a = apply(((C,1,2,3),('m0',1,2),('m0',1,2),('m0',1,2),('m0',1,2)))
print(a)