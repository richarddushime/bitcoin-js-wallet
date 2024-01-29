from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic

def create_wallet():
    # Generate a new mnemonic
    mnemonic = Mnemonic().generate()

    # Create a wallet from the mnemonic
    wallet = Wallet.create('richarddushime', witness_type='segwit', keys=mnemonic , network='testnet')

    # Get the first key in the wallet
    key = wallet.get_key()

    # Print the wallet details
    print("| Public Address |", key.address, "|")
    print("| Private Key     |", key.wif, "|")

    # Save wallet details to a file
    with open('py-wallet.json', 'w') as file:
        file.write('{"address": "' + key.address + '", "privateKey": "' + key.wif + '"}')

if __name__ == "__main__":
    create_wallet()
