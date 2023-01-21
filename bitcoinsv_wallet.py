#!/usr/bin/env python3
from bitsv import Key, PrivateKey
network = "main"
my_key_test = PrivateKey(network=network)
print(my_key_test.address)
print(my_key_test.to_hex())
print(my_key_test.to_wif())