''' u niej to jest Esercizio su __mro__ '''

class ClassB():

    def countVarClass(self,t,n):
        result = 0
        meta_class_nr = 0
        for meta_class in self.__class__.__mro__:
            vars_class = [var for var in vars(meta_class) if var[0] != '_' and not callable(getattr(meta_class,var))]
            for var in vars_class:
                if type(getattr(meta_class,var)) == t:
                    result += 1
            meta_class += 1
            if meta_class_nr == n:
                return result
        return result


