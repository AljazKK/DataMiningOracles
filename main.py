from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/41b43a4321934a4aa1bb9c23dd7598d0"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0x240BaE5A27233Fd3aC5440B5a598467725F7D1cd")
print(web3.fromWei(balance, "ether"))

