#!/usr/bin/env python3
from bitsv import Key, PrivateKey
#from whatsonchain.api import Whatsonchain

# Small Molly https://bico.media/fa30c0e1384fc78204d259c0957676c403ea73f04777bc54a9dc7e2f3af70d70
# Large Molly https://bico.media/db8063c6c806ec1a2ddcc1005f4b9dbcef110c3c83c3cb28abf87ad0fc46b812

#Example output from https://github.com/unwriter/B
#OP_RETURN
#  19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut
#  [Data]
#  [Media Type]
#  [Encoding]
#  [Filename]

#B Crap example
#OP_RETURN 19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut  <html><body>hello world</body></html>  text/html  UTF-8  hello.html

my_key = Key.from_hex('1965714ec753091ec034bc44e6cb0e6adbe453ee6893a0f8ffb13924705f9377', network='main')

with open("docs/images/mollycat-lg.gif", "rb") as fp:
    molly_binary = fp.read()

list_of_pushdata = [
    "19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut".encode('utf-8'),
    molly_binary,
    "image/gif".encode('utf-8'),
    "binary".encode('utf-8'),
    "molly.gif".encode('utf-8')
]

txid = my_key.send_op_return(list_of_pushdata)

print(txid)
