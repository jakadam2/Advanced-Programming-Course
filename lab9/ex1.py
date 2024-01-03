'''slajd3'''

def myDecorator(obj):
    def countVarClass(self,t):
        counter = 0
        variables = list(vars(self).values())
        for var in variables:
            if type(var) == t:
                counter += 1
        return counter
    obj.countVarClass = countVarClass
    return obj
