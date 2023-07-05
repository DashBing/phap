__all__ = [
    "base",
    "json",
    "hash",
]

def hex_to_int(text:str) -> int:
    odata = 0; text = text.upper();
    for c in text:
        tmp = ord(c)
        if tmp <= ord('9'):
            odata = odata << 4; odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4; odata += tmp - ord('A') + 10
    return odata
