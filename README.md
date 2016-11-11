Insight Data Engineering - Paymo Digital Wallet
===========================================================
My solution to the [coding challenge](https://github.com/InsightDataScience/digital-wallet) for the [Insight Data Engineering Program](http://insightdataengineering.com/) implemented in Python 2.7

## Dependencies 
- Python 2.7 (2.7.10)
- [NetworkX] (https://networkx.github.io/): a Python package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks.
	- Quick install: `pip install networkx`. [Installing Doc] (https://networkx.readthedocs.io/en/stable/install.html)

##  Environments
- Tested on MacOS (10.12.1)

## Optional Features
This solution can take on degrees greater than 4. 

- The first param (i.e. `sys.argv[1]`) of the calling script is used for specifying the degree. 
- For instance, calling the script with degree 2 would be `python ./src/antifraud.py 2 ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output2.txt`

## Tests
1. Normal `trusted` transaction.
2. Normal `unverified` transaction.
3. One "sending money to myself" transaction (expects `trusted`).
4. Graph as a flat tree, then form a loop graph from the tree, and verify transactions.
5. Using the flat tree to test solution's integrity of different degrees.
6. Two unconnected cliques, then connect them, and verify transactions.
7. A random scenario.

## Owner
- Tanakrit Supanaraphan