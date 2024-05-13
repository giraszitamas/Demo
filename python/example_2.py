from web3 import Web3
import json
url = "http://127.0.0.1:7545"
connection = Web3(Web3.HTTPProvider(url))


account_1 = "0xAA3CdC1BdAD42861FFfd227A75ddeF1Ffd7Cc295"
private_key = "0x62351e8a4463e4e0f9c7e40fa8a09fff3560e5de55c2c576e45aed9af7ad1d40"

abi =json.loads('[ { "inputs": [ { "internalType": "int256", "name": "_value", "type": "int256" } ], "name": "set", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "get", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" } ]')
contract_address = connection.to_checksum_address("0x76ff69Fa57a24DA4e4d409DcE79EC4b0C5491959")


contract = connection.eth.contract(address=contract_address, abi = abi)

print(contract.functions.get().call())