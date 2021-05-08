import requests
import chardet
import idna
from decimal import Decimal
import certifi
import time
import pandas as pd


address = "0x240BaE5A27233Fd3aC5440B5a598467725F7D1cd"
start_block = 12250000
end_block = 12400000
#mind the API KEY (end of url)

data = pd.DataFrame()

for i in range(end_block, start_block, -10000):
    url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + address + \
      "&startblock="+ str(i-10000) + "&endblock="+ str(i) + "&sort=desc&apikey=V95KZCDIMQZMB885H5X9H2UD1HG1SJWSNC"

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
        tansaction_index = transaction.get("transactionIndex")
        gas = transaction.get("gas")
        LINK_value = Decimal(value) / Decimal("1000000000000000000")  # calculation to LINK
        gas_price = transaction.get("gasPrice")
        gas_used = transaction.get("gasUsed")
        transaction_fee = Decimal(gas_price)*Decimal(gas_used)/Decimal("1000000000000000000")
        cumulativeGasUsed = transaction.get("cumulativeGasUsed")
        input_trans = transaction.get("Input")


    data_new = pd.DataFrame(
        {
            'block_no': [block_no],
            'timestamp': [timestamp],
            'hash': [hash],
            'tx_from': [tx_from],
            'contract_address': [contract_address],
            'tx_to': [tx_to],
            'value': [value],
            'tokenName': [tokenName],
            'token_decimal': [token_decimal],
            'tansaction_index': [tansaction_index],
            'gas': [gas],
            'LINK_value': [LINK_value],
            'gas_price': [gas_price],
            'gas_used': [gas_used],
            'transaction_fee': [transaction_fee],
            'cumulativeGasUsed': [cumulativeGasUsed],
            'input': [input_trans]
        }
    )

    data = pd.concat([data, data_new])

print(data)

data.to_csv("C:/Users/kalin/Documents/UZH Master Thesis/data etherscan/LinkPool.csv")

