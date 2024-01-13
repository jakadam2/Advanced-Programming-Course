def decFact(*argss,**kwargss):
    def dec(obj):
        old_init = obj.__init__
        def new_init(self,*args,**kwargs):
            for i in range(len(argss)):
                setattr(self,argss[i],None)
            for key in kwargss:
                setattr(self,key,kwargss[key])
            old_init(self,*args,**kwargs)
        obj.__init__ = new_init
        return obj 
    return dec
