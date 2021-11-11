import json
import requests

url = "https://evmexplorer.velas.com/rpc"
headers = {'content-type': 'application/json'}
# Example echo method JSON-RPC 1.0
payload = {"method":"eth_getTransactionCount","params":["0x8E6d9C2aE9F29Ee7f434D49565D704f1bDFeb933"],"id":1,"jsonrpc":"2.0"}

response = requests.post(url, data=json.dumps(payload), headers=headers).json()

print(response)
print(int(0x2962))



