import hashlib


def sha256(d: bytes, hex=False):
    assert type(d) == bytes, 'd must be of type bytes.'
    m = hashlib.sha256()
    m.update(d)
    return m.hexdigest() if hex else m.digest()

