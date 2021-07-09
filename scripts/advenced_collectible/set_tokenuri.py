from brownie import AdvancedCollectible, network, accounts, config
from scripts.helpful_scripts import get_breed

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def main():
    print("Working on " + network.show_active())
    advanced_colletible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_colletibles = advanced_colletible.tokenCounter()
    print("Liczba tokenow ktore stworzyles: " + str(number_of_advanced_colletibles))
    for token_id in range(number_of_advanced_colletibles):
        breed = get_breed(advanced_colletible.tokenIdToBreed(token_id))
        if not advanced_colletible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, advanced_colletible, dog_metadata_dic[breed])
        else:
            print("Oposczamy {}, juz ustaliwilismy ten tokenURI!".format(token_id))

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Swietnie! mozesz zobaczy swoj token NFT pod adresem {}".format(OPENSEA_FORMAT.format(nft_contract.address, token_id))
    )
    print("Prosze poczekaj okolo 20 min i nacisnij przycisk 'refresh metadata'")