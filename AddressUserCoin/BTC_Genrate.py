from bitcoinlib.wallets import Wallet as WallB ,wallet_delete_if_exists
from bitcoinlib.mnemonic import Mnemonic

def BTC_Gen(NameW):
    if wallet_delete_if_exists(NameW): pass
    passphrase = Mnemonic().generate()
    wall = WallB.create(NameW, keys=passphrase, network='bitcoin')
    BTC_add=wall.get_key().address
    return BTC_add