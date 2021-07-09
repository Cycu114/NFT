#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed, fund_advanced_collectible
import time


STATIC_SEED = 123


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    fund_advanced_collectible(advanced_collectible)
    transaction = advanced_collectible.createCollectible(
    STATIC_SEED, "NONE" , {"from": dev}
    )
    print("Oczekiwanie na traanskacje...")
    # wait for the 2nd transaction
    transaction.wait(1)
    time.sleep(80)
    requestId = transaction.events["requestedCollectible"]["requestId"]
    token_id = advanced_collectible.requestIdToTokenId(requestId)
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    print("Rasa psa o tokenie {} is {}".format(token_id, breed))
