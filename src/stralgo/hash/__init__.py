from hashlib import md5 as _m5
from .sha import *
from .sm import *

def md5(data:bytes) -> str:
    return(_m5(data).hexdigest())

def text_md5(text:str, encoding:str="utf-8") -> str:
    return(md5(text.encode(encoding)))
t_md5 = text_md5
