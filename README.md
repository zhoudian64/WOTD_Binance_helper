# WOTD Binance helper

This is a simple script that helps users to pass Binance Word Of ToDay.

## usage

``` shell
# remember to install nltk
python -m pip install nltk
python main.py <filepath> <word length> <forbidden_letters> <required_letters>
```

## example
You can easily give the article and word length of WOTD into that before adding forbidden or required letters.

Like 
``` shell
python main.py ETH_UPGRADE.txt 5
# that may output
might
miner
named
other
party
phase
piece
price
their
```
Choose a word with most different letters to WOTD, and get response from Binance.
Just like, fill in with `PRICE`, and Binance may tell u `rie` are yellow, `pc` are grey.
You can then again operate like:
```shell
python main.py ETH_UPGRADE.txt 5 pc rie
Filtered Words:
miner
their
```


## buy me a cup of coffee

```
BTC: 15GYRbTv2w5RqowNX8j9w8TziLyWKzumAu
BTC(BNB Smart Chain BEP20): 0xab6b7b20915cc4ac2a56b9fdd07de986388cac72
BNB(BNB Smart Chain BEP20): 0xab6b7b20915cc4ac2a56b9fdd07de986388cac72
USDT(AVAXC AVAX C-Chain): 0xab6b7b20915cc4ac2a56b9fdd07de986388cac72
```

GLHF to all BTC and BNB HODLERs. 