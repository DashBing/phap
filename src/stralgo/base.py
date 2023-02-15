from base64 import b16encode as _b16e
from base64 import b16decode as _b16d
from base64 import b32encode as _b32e
from base64 import b32decode as _b32d
from base64 import b64encode as _b64e
from base64 import b64decode as _b64d
from base64 import b85encode as _b85e
from base64 import b85decode as _b85d

class base16:
    def encode(data:bytes) -> str:
        return(_b16e(data).decode())
    def decode(data:str) -> bytes:
        return(_b16d(data.encode()))

class base32:
    def encode(data:bytes) -> str:
        return(_b32e(data).decode())
    def decode(data:str) -> bytes:
        return(_b32d(data.encode()))

class base64:
    def encode(data:bytes) -> str:
        return(_b64e(data).decode())
    def decode(data:str) -> bytes:
        return(_b64d(data.encode()))

class base85:
    def encode(data:bytes) -> str:
        return(_b85e(data).decode())
    def decode(data:str) -> bytes:
        return(_b85d(data.encode()))
