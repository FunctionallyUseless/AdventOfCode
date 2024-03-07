import hashlib

def generate_key(key, nonce):
    concat_key = key + str(nonce)
    return bytes(concat_key, "utf-8")

def verify_hex(substring: str, fullstring: str) -> bool:
    return fullstring.startswith(substring)

def part_one() -> int:
    KEY = 'ckczppom'
    nonce = 0

    while True:
        test_key = generate_key(KEY, nonce)
        h = hashlib.new('md5')
        h.update(test_key)
        hexdigest = h.hexdigest()
        if verify_hex("00000", hexdigest):
            return nonce

        nonce += 1

def part_two() -> int:
    KEY = 'ckczppom'
    nonce = 0

    while True:
        test_key = generate_key(KEY, nonce)
        h = hashlib.new('md5')
        h.update(test_key)
        hexdigest = h.hexdigest()
        if verify_hex("000000", hexdigest):
            return nonce

        nonce += 1
