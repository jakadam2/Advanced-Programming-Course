'''slajd5'''
def make_base(obj):
    obj.varC = 1000
    def f(self,v):
        print(v * self.varl)
    def g(x):
        print(x * obj.varC)
    obj.f = f
    obj.g = staticmethod(g)
    old_init = obj.__init__
    def new_init(self,*args,**kwargs):
        self.varl = 10
        old_init(self,*args,**kwargs)
    obj.__init__ = new_init
    return obj



