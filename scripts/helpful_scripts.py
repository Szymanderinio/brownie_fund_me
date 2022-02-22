from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENV = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV or network.show_active() in FORKED_LOCAL_ENV:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_price_feed_eth_usd(account):
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks(account)
        return MockV3Aggregator[-1].address


def deploy_mocks(account):
    print("The active network is {}".format(network.show_active()))
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": account})
    print("Mocks Deployed!")


def get_if_in_dev():
    return config["networks"][network.show_active()]["verify"]
