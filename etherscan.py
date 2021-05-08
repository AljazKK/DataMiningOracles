import requests
import chardet
import idna
from decimal import Decimal
import certifi

address = "0x240BaE5A27233Fd3aC5440B5a598467725F7D1cd"
start_block = 12370000
end_block = 99999999

url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + address + \
      "&startblock="+ str(start_block) + "&endblock="+ str(end_block) + "&sort=desc&apikey=V95KZCDIMQZMB885H5X9H2UD1HG1SJWSNC"


response = requests.get(url, verify = certifi.where())

address_content = response.json()
print(address_content)

result = address_content.get("result")

for transaction in result:
      block_no = transaction.get("blockNumber")
      timestamp = transaction.get("timeStamp")
      hash = transaction.get("hash")
      tx_from = transaction.get("from")
      contract_address = transaction.get("contractAddress")
      tx_to = transaction.get("to")
      value = transaction.get("value")
      tokenName = transaction.get("tokenSymbol")
      token_decimal = transaction.get("tokenDecimal")
      transaction_index = transaction.get("transactionIndex")
      gas = transaction.get("gas")
      LINK_value = Decimal(value) / Decimal("1000000000000000000")  # calculation to LINK
      gas_price = transaction.get("gasPrice")
      gas_used = transaction.get("gasUsed")
      transaction_fee = Decimal(gas_price)*Decimal(gas_used)/Decimal("1000000000000000000")
      cumulativeGasUsed = transaction.get("cumulativeGasUsed")
      input = transaction.get("Input")

      print("block number: ", block_no)
      print("timestamp: ", timestamp)
      print("hash: ", hash)
      print("from: ", tx_from)
      print("Contract address: ", contract_address)
      print("to: ", tx_to)

      if tx_from == address: #calculation to say if address received or send the transaction
            print("OUT")
      else:
            print("IN")

      print("value: ", value)
      print("Token: ", tokenName)

      print("LINK value: ", LINK_value)
      print("transaction index: ", transaction_index)
      print("gas: ", gas)
      print("gas price: ", gas_price)
      print("gas used: ", gas_used)
      print("Cummulative gas used: ", cumulativeGasUsed)
      print("transaction fee in ETH: ", transaction_fee)
      print("Input data: ", input)
      print("\n")
