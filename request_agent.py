
import json


with open('keys.json') as f:
    keys = json.load(f)

import requests

def do_faucet_request(address, url='http://localhost:5555/claim', ):
    """curl -X 'POST' localhost:5555/claim -H "Content-Type: application/json" -d '{"public_address": "0xC1AEEF1074C193e2331B16D7dc1dA107387F73b4", "ledger_id": "neon-testnet"}'
{"result": "Success! Please await transaction confirmation."}
"""
    res = requests.post(
        url,
        json={
            'public_address': address,
            'ledger_id': 'neon-testnet'
        }
    )
    print(res.json())

for key_pair in keys[:25]:
    address = key_pair['address']
    do_faucet_request(address)

