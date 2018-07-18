import nacl
import nacl.encoding
import nacl.signing


def verify(v: str, msg, sig):
    v = bytes.fromhex(v)
    sig = bytes.fromhex(sig)
    v = nacl.signing.VerifyKey(v)
    try:
        v.verify(msg, sig)
    except nacl.exceptions.BadSignatureError:
        return False
    except Exception:
        return False
    return True
