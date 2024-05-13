from web3 import Web3
import json
url = "http://127.0.0.1:7545"
connection = Web3(Web3.HTTPProvider(url))

new_account = connection.eth.account.create()

print("Address:", new_account.address)
print("Private Key:", new_account.key.hex())
print("Balance:",connection.eth.get_balance(new_account.address))

account_1 = "0xAA3CdC1BdAD42861FFfd227A75ddeF1Ffd7Cc295"
private_key = "0x62351e8a4463e4e0f9c7e40fa8a09fff3560e5de55c2c576e45aed9af7ad1d40"

tx = {
    'nonce' : connection.eth.get_transaction_count(account_1),
    "to" : new_account.address,
    "value": connection.to_wei(4,"ether"),
    "gas" : 2000000,
    "gasPrice" : connection.to_wei(50,"gwei")
}

signed_tx = connection.eth.account.sign_transaction(tx, private_key)
tx_hash   = connection.eth.send_raw_transaction(signed_tx.rawTransaction)

print("Balance aftre transaction:",connection.eth.get_balance(new_account.address))