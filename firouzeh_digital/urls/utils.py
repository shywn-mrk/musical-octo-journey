import string

BASE62_ALPHABET = string.digits + string.ascii_letters

def base62_encode(num, length=7):
    base = len(BASE62_ALPHABET)
    encoded = ''
    while num > 0:
        num, rem = divmod(num, base)
        encoded = BASE62_ALPHABET[rem] + encoded

    return encoded.zfill(length)
