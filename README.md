# bsv_bsnake
BSV B:// Snake!! ![pythonglogo](/docs/images/Python-logo-notext.svg.png)
=================
Put your images and other media on the BSV blockchain.

![MollyCat](/docs/images/mollycat.gif)

Python script to run transactions using the B protocol 

![VSCode](/docs/images/vscode_testnet_txid.jpg)
Run `bitsv_b_test.py` to put your image on the block chain. Copy the txid output and find it on the [Whatsonchain](https://test.whatsonchain.com/tx/9cd2e294b71e2c2b220dbe6f6dd4026fe5c97f6392d85ef5813a3f66dc672623) block explorer. 

In `bitsv_b_test.py` line 19 `network='test')`
Change `test` to `main` to put your image on the MainNet. 

![Block](/docs/images/woc_testnet_block_explorer.jpg)

Add your txid into the block exploer. 

![Decode](/docs/images/woc_testnet_decode_button.jpg)

Select the `Decode` button to show your image.

![Image on the TestNet](/docs/images/woc_decode.jpg)
This is the image on the TestNet BSV blockchain. [Molly Cat](https://plugins-test.whatsonchain.com/api/plugin/main/9cd2e294b71e2c2b220dbe6f6dd4026fe5c97f6392d85ef5813a3f66dc672623/0) link to WOC TestNet.

Run `bitcoinsv_wallet.py` to create your own wallet. 

Private key is in the file for all to test. 

Here is the image on Main: 
https://bico.media/db8063c6c806ec1a2ddcc1005f4b9dbcef110c3c83c3cb28abf87ad0fc46b812


Other:

`bitsv_b_test.py` reads the binary for you in line 25. 
```
with open("docs/images/mollycat-lg.gif", "rb") as fp:
    molly_binary = fp.read()
```

Each number is associated with a character if you look at the [ASCII table](https://www.asciitable.com/).
![Binary](/docs/images/binary.jpg)
![ASCII table](/docs/images/ascii_table.gif)