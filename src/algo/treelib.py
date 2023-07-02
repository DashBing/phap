from phap import ErrorTemplate

class ValueTypeError(ErrorTemplate):
    message = "The value's type must not be treenode."
    info_list = ['Try to change the type to "str" or "int".']

class treenode:
    def __init__(self, val = 0, left = 0, right = 0):
        self.__t = [str(self.__class__)]
        if str(type(val)) in self.__t:
            self.val = 0
            raise ValueTypeError()
        else:
            self.val = val
        self.left = left
        self.right = right
    def setfromlist(self, val:list):
        self.val = val[0]
        if str(type(val[1])) == str(type([])):
            self.left = treenode().setfromlist(val[1])
        else:
            self.left = val[1]
        if str(type(val[2])) == str(type([])):
            self.right = treenode().setfromlist(val[2])
        else:
            self.right = val[2]
    def getlist(self) -> list:
        l = []
        l.append(self.val)
        if str(type(self.left)) in self.__t:
            l.append(self.left.getlist())
        else:
            l.append(self.left)
        if str(type(self.right)) in self.__t:
            l.append(self.right.getlist())
        else:
            l.append(self.right)
        return(l)
    #def getnode(self) -> str:
    #    l = self.getlist()
    #    return("")
    #def __str__(self) -> str:
    #    return(self.getnode())
