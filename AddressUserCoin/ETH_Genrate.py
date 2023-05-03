from eth_keys import keys
import random
import string

def ETH_Gen(NameW):
    letters = string.ascii_lowercase
    RandStr = NameW.join(random.choice(letters) for i in range(10))
    arrSig = bytes(RandStr[:32], 'utf-8')
    priv_key = keys.PrivateKey(arrSig)
    ETH_add = priv_key.public_key.to_checksum_address()
    return ETH_add