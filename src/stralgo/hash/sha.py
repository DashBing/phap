from hashlib import sha256 as _s2
from hashlib import sha512 as _s5

def sha256(data:bytes) -> str:
    return(_s2(data).hexdigest())

def sha512(data:bytes) -> str:
    return(_s5(data).hexdigest())

def text_sha256(text:str, encoding:str="utf-8") -> str:
    return(sha256(text.encode(encoding)))
t_sha256 = text_sha256

def text_sha512(text:str, encoding:str="utf-8") -> str:
    return(sha512(text.encode(encoding)))
t_sha512 = text_sha512
