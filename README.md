# bsv_bsnake
BSV B:// Snake!! ![pythonglogo](/docs/images/Python-logo-notext.svg.png)
=================
Put your images and other media on the BSV blockchain. Thanks to [BitSV](https://github.com/AustEcon/bitsv) and [B://](https://github.com/unwriter/B)

![MollyCat](/docs/images/mollycat.gif)

Python script to run transactions using the B protocol 

* You will need to install [bitsv](https://github.com/AustEcon/bitsv) python libray. 

## Basic Instructions

Run bsv_b_test.py:

```
python3 bitsv_b_test.py
```


## Other Details
![VSCode](/docs/images/vscode_testnet_txid.jpg)




Run `bitsv_b_test.py` to put your image on the block chain. Copy the txid output and find it on the [Whatsonchain](https://test.whatsonchain.com/tx/9cd2e294b71e2c2b220dbe6f6dd4026fe5c97f6392d85ef5813a3f66dc672623) block explorer. 


## Trying Testnet and Mainnet TBSV & BSV

In `bitsv_b_test.py` line 19 `network='test')`
Change `test` to `main` to put your image on the MainNet. 

## Find your transaction on the Block Explorers

![Block](/docs/images/woc_testnet_block_explorer.jpg)

Add your txid into the block exploer. 

![Decode](/docs/images/woc_testnet_decode_button.jpg)

Select the `Decode` button to show your image.

![Image on the TestNet](/docs/images/woc_decode.jpg)
This is the image on the TestNet BSV blockchain. [Molly Cat](https://plugins-test.whatsonchain.com/api/plugin/main/9cd2e294b71e2c2b220dbe6f6dd4026fe5c97f6392d85ef5813a3f66dc672623/0) link to WOC TestNet.

## Need more wallets? 

Run `bitcoinsv_wallet.py` to create your own wallet. 

Private key is in the file for all to test. 

## Bico.media block explorer 

Here is the image on Main: 
https://bico.media/db8063c6c806ec1a2ddcc1005f4b9dbcef110c3c83c3cb28abf87ad0fc46b812


## How this works? Binary

`bitsv_b_test.py` reads the binary for you in line 25. 
```
with open("docs/images/mollycat-lg.gif", "rb") as fp:
    molly_binary = fp.read()
```

Each number is associated with a character if you look at the [ASCII table](https://www.asciitable.com/).
![Binary](/docs/images/binary.jpg)
![ASCII table](/docs/images/ascii_table.gif)