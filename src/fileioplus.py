from random import randint
from phap import TypeErrorTemplate

modelist = {
    "r":["r","r+","rb","rb+"],
    "w":["w","w+","wb","wb+"],
    }

class ModeNotFoundError(TypeErrorTemplate):  # 没有找到此文件打开模式
    message = "This mode is not a legal file opening mode"
    info_list = ["Try to change a new mode to open the file."]

class open_r:
    def __init__(self,
                 file,
                 mode = "r",
                 buffering: int = -1,
                 encoding: str | None = None,
                 errors: str | None = None,
                 newline: str | None = None,
                 closefd: bool = True,
                 opener = None):
        self.name = file
        self.mode = mode
        #elf.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newlines = newline
        #self.closefd = closefd
        #self.opener = opener
        self.__checkvaluedict = {
            "name":file,
            "mode":mode,
            "encoding":encoding,
            "errors":errors,
            "newlines":newline,
        }
        self.__fileobj = open(file=file,mode=mode,buffering=buffering,encoding=encoding,errors=errors,newline=newline,closefd=closefd,opener=opener)
    def __del__(self):
        self.close()
    def close(self):
        self.__fileobj.close()
    def _checkvalue(self):
        pass
        #n = 0
        #if self.__checkvaluedict[""]

class open_w(open_r):
    pass

def open(
        file,
        mode = "r",
        buffering: int = -1,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
        closefd: bool = True,
        opener = None):
    if mode in modelist["r"]:
        return open_r(file=file,mode=mode,buffering=buffering,encoding=encoding,errors=errors,newline=newline,closefd=closefd,opener=opener)
    elif mode in modelist["w"]:
        return open_w(file=file,mode=mode,buffering=buffering,encoding=encoding,errors=errors,newline=newline,closefd=closefd,opener=opener)
    else:
        raise ModeNotFoundError(msgtype=mode)
