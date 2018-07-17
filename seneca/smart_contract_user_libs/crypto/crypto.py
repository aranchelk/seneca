import hashlib
from functools import partial

'''
    Highly abstracted hashing library that exposes the algorithms guaranteed by hashlib a la Python 3.
    These functions are the following: blake2b, shake_128, sha3_384, sha3_224, shake_256, md5, sha256, 
    sha512, sha1, sha224, sha3_256, blake2s, sha3_512, sha384
'''


def hash_data(d: bytes, algo: str, as_hex=False):
    assert algo in hashlib.algorithms_guaranteed
    assert type(d) == bytes, 'd must be of type bytes.'

    m = hashlib.new(algo)
    m.update(d)
    return m.hexdigest() if as_hex else m.digest()


def f(algo: str):
    assert algo in hashlib.algorithms_guaranteed

    return partial(hash_data, algo=algo)


exports = {
    key: f(key) for key in hashlib.algorithms_guaranteed
}