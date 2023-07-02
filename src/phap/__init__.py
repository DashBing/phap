import algo
import stralgo
from random import randint

class ErrorTemplate(Exception):  # 错误模板
    message = ""
    info_list = []
    info_tips = "Detailed information: "
    def __init__(self, info:str = None):
        if info != None:
            self.message = self.message + "\n%s%s"%(self.info_tips,info)
        elif len(self.info_list) > 0:
            self.message = self.message + "\n%s%s"%(self.info_tips,self.info_list[randint(0,len(self.info_list)-1)])
    def __str__(self) -> str:
        return(self.message)

class TypeErrorTemplate(ErrorTemplate):  # 带有提示信息的错误模板
    def __init__(self, msgtype:str = None, info:str = None):
        if msgtype == None:
            self.message = self.message + "."
        else:
            self.message = self.message + ": <%s>"%msgtype
        super().__init__(info=info)
