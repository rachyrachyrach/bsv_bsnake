#!/usr/bin/env python3
from bitsv import Key, PrivateKey
#from whatsonchain.api import Whatsonchain


#OP_RETURN
#  19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut
#  [Data]
#  [Media Type]
#  [Encoding]
#  [Filename]

#B Crap
#OP_RETURN 19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut  <html><body>hello world</body></html>  text/html  UTF-8  hello.html

my_key = Key.from_hex('e80e48bc6eb32dc0f323f69a14f82bd1b32cbaed8308284e9d3b58cdb5d9dcf2', network='test')


#my_key = Key('e80e48bc6eb32dc0f323f69a14f82bd1b32cbaed8308284e9d3b58cdb5d9dcf2', network='test')
list_of_pushdata = [
    bytes.fromhex('6d01'),
    'New_Name'.encode('utf-8')]

list_of_pushdata = [
    "19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut".encode('utf-8'),
    "<html><body>hello world</body></html>".encode('utf-8'),
    "text/html".encode('utf-8'),
    "UTF-8".encode('utf-8'),
    "hello.html".encode('utf-8')
]

txid = my_key.send_op_return(list_of_pushdata)

print(txid)
