from brownie import FundMe
from .helpful_scripts import *

def deploy_fund_me():
    account = get_account()
    price_feed = get_price_feed_eth_usd(account)
    fund_me = FundMe.deploy(price_feed, {"from": account}, publish_source=get_if_in_dev(),)
    print("Contract deployed to {}".format(fund_me.address))
    return fund_me

def main():
    deploy_fund_me()
    # brownie compile !!!
    # brownie run scripts/deploy.py --network kovan
    # brownie test
    # brownie console !!!
