from web3 import Web3
import json
url = "http://127.0.0.1:7545"
connection = Web3(Web3.HTTPProvider(url))

account_1 = "0xAA3CdC1BdAD42861FFfd227A75ddeF1Ffd7Cc295"
account = connection.eth.account.from_key("0x62351e8a4463e4e0f9c7e40fa8a09fff3560e5de55c2c576e45aed9af7ad1d40")

connection.eth.default_account = account_1

abi =json.loads('[ { "inputs": [ { "internalType": "int256", "name": "_value", "type": "int256" } ], "name": "set", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "get", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" } ]')
contract_address = connection.to_checksum_address("0xcC03299880357454A80B89B0AeB7212b7aA84D47")

contract = connection.eth.contract(address=contract_address, abi = abi)

print(contract.functions.set(456).transact())
print(connection.eth.get_balance(account_1))