from web3 import Web3

url = "http://127.0.0.1:7545"
connection = Web3(Web3.HTTPProvider(url))

account_1 = "0xAA3CdC1BdAD42861FFfd227A75ddeF1Ffd7Cc295"
account_2 = "0x2e289a5BE0a98c618cC27bF90ac9F25Df65CD6cF"

private_key = "0x62351e8a4463e4e0f9c7e40fa8a09fff3560e5de55c2c576e45aed9af7ad1d40"

tx = {
    'nonce' : connection.eth.get_transaction_count(account_1),
    "to" : account_2,
    "value": connection.to_wei(1,"ether"),
    "gas" : 2000000,
    "gasPrice" : connection.to_wei(50,"gwei")
}

signed_tx = connection.eth.account.sign_transaction(tx, private_key)
tx_hash   = connection.eth.send_raw_transaction(signed_tx.rawTransaction)
print(connection.to_hex(tx_hash))
