def to_hex(b):
    if type(b) == bytes:
        return '0x' + bytes.hex(b)
    elif type(b) == int:
        return hex(b)
    elif type(b) == str:
        s = b.encode()
        return '0x' + bytes.hex(s)
    else:
        return None


def to_bytes(b):
    if type(b) == str:
        if b[:2] == '0x':
            return bytes.fromhex(b[2:])
        return b.encode()
    elif type(b) == int:
        h = hex(b)
        return bytes.fromhex(h[2:])
    else:
        return None


def to_int(b):
    if type(b) == str:
        if b[:2] == '0x':
            return int(b[2:], 16)
        h = to_hex(b)
        return int(h[2:], 16)
    if type(b) == bytes:
        return int(bytes.hex(b), 16)
    else:
        return None
