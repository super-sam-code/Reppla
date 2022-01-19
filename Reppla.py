from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/a0a35f3afb8f44fb9a66f9e1ee2f4bbe"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())