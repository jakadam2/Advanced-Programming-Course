class C:

    a = 'sssaas'
    b = 3
    d = 'dADASDASDASDAS'

    def __init__(self) -> None:
        self.c = 'asdasdasd'

    @classmethod
    def addProperty(cls):
        variables = [var for var in vars(cls) if var[0] != '_' and not callable(getattr(cls,var))]
        for var in variables:
            if type(getattr(cls,var)) == str:
                value = getattr(cls,var)
                print(var)
                def get(cls,var = var):
                    return getattr(cls,f'_{str(var)}')

                def set(cls,val,var = var):
                    if type(val) != str:
                        raise AttributeError(f'It is no possibility to set attribute {var} to {val}')
                    setattr(cls,f'_{str(var)}',val)

                setattr(cls,f'_{str(var)}',value)
                setattr(cls,str(var),property(get,set))
                