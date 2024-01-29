# Generating a Testnet P2WPKH (SegWit) Wallet in Python

#### Dependencies:
- `bitcoinlib`: A Python library for working with Bitcoin.

#### Installation:
Ensure that you have the required dependencies installed before running the program:

```
pip install python-bitcoinlib
```

#### How to Run the Program:
First Fork the repository and Give it a stars if you like it
1. clone this repository 
 ```
 git clone https://github.com/richarddushime/bitcoin-js-wallet.git
 ```
2. Open a terminal and navigate to the directory containing the script.
```
cd bitcoin-js-wallet
```
3. Run the script using the following command:

```bash
python3 wallet.py
```

#### Results:
Upon successful execution, the program performs the following actions:
- Generates a new mnemonic.
- Creates a Testnet P2WPKH (SegWit) wallet using the generated mnemonic.
- Prints the public address and private key of the first key in the wallet.
- Saves the wallet details to a JSON file named `py-wallet.json`.

The generated wallet details can be used for further Bitcoin-related activities on the Testnet.


# Creating a Testnet P2PKH Wallet using bitcoinjs-lib


#### Dependencies:
- [bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib): A JavaScript library for working with Bitcoin.
- [ecpair](https://www.npmjs.com/package/ecpair): A library for creating elliptic curve key pairs.
- [tiny-secp256k1](https://www.npmjs.com/package/tiny-secp256k1): A library for working with the secp256k1 elliptic curve.
- [fs](https://nodejs.org/api/fs.html): Node.js filesystem module.

#### Installation:
Before running the program, ensure that you have `Node.js` and `npm` installed. Then, install the required dependencies by running the following command:

```
npm install bitcoinjs-lib ecpair tiny-secp256k1
```

#### How to Run the Program:

Execute the following command in the terminal to run the script and create a Testnet P2PKH wallet:

```
node wallet.js
```

#### Results:
The program will generate a random key pair, derive the Bitcoin address from the public key, print the public address and private key to the console, and save the wallet details to a JSON file named `wallet.json`. The file structure will be similar to the following:

```json
{
    "address": "1D6xsXae...",
    "privateKey": "L1Tugb42..."
}
```

Note: The program is currently set to use the Bitcoin Testnet; you can modify the `network` variable to `bitcoin.networks.mainnet` or `bitcoin.networks.regtest` for the mainnet or regtest, respectively.


