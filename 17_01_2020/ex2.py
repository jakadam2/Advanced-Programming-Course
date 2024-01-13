def dectFact(L1,L2):
    def dec(obj):
        assert(len(L1) == len(L2))
        old_init = obj.__init__
        def new_init(self,*args,**kwargs):
            for i in range(len(L1)):
                setattr(self,L1[i],L2[i])
            old_init(self,*args,**kwargs)
        obj.__init__ = new_init
        return obj
    return dec
