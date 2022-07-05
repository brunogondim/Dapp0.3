import json
from web3 import Web3

def hex2str(hex):
    return bytes.fromhex(hex[2:]).decode("utf-8")

def str2hex(str):
    return "0x" + str.encode("utf-8").hex()

web3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

adress_file = open("../deployments/localhost/dapp.address",'r')
rollups_address = adress_file.read()
    
input_abi_file = open("../deployments/localhost/InputFacet.json",'r')
input_abi_json = json.load(input_abi_file)
input_abi = input_abi_json["abi"]

input_contract = web3.eth.contract(abi=input_abi, address=rollups_address)
