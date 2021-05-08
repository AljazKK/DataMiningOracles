import requests
import chardet
import idna
from decimal import Decimal
import certifi
import time
import pandas as pd
from panda import DataFrame

data = pd.DataFrame({'block_no': [],

                     'hash': [],

                     'from': [], "gas":[]})

address = "0x4565300C576431e5228e8aA32642D5739CF9247d"
start_block = 12200000
end_block = 12500000
api_key = V95KZCDIMQZMB885H5X9H2UD1HG1SJWSNC

for i in range(12500000, 12200000, -10000):
    url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + \
          "&startblock=" + str(i - 10000) + "&endblock=" + str(i) + "&sort=asc&apikey=V95KZCDIMQZMB885H5X9H2UD1HG1SJWSNC"

    response = requests.get(url, verify=certifi.where())

    address_content = response.json()
    # print(address_content)

    result = address_content.get("result")
    print(result)
    for transaction in result:
        block_no = transaction.get("blockNumber")
        hast = transaction.get("hash")
        tx_from = transaction.get("from")
        tx_to = transaction.get("to")
        value = transaction.get("value")
        gas = transaction.get("gas")
        input = transaction.get("Input Data:")

        print("block number: ", block_no)
        print("hash: ", hast)
        print("from: ", tx_from)
        print("to: ", tx_to)

        if tx_from == address:  # calculation to say if address received or send the transaction
            print("OUT")
        else:
            print("IN")

        print("value: ", value)
        eth_value = Decimal(value) / Decimal("1000000000000000000")  # calculation to eth

        print("eth value: ", eth_value)
        print("gas: ", gas)
        print("Input data: ", input)
        print("\n")

        for i in range(5):
            new_data = pd.DataFrame(data={'block_no': [block_no],
                                          'hash': [hast],
                                          'from': [tx_from],"gas":[gas]})
            data = pd.concat([data, new_data])


data.to_csv("C:/Users/kalin/Documents/UZH Master Thesis/data etherscan/blablabla.csv", index = False)
print(data)
