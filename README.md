Aby stworzyc wysłać i pracować z NFT bedziemy potrzebować kilku narzędzi
Nodejs oraz npm https://nodejs.org/en/download/
python https://www.python.org/downloads/

w pierwzsej kolejnosci musimy zasintalowac brownie
pip install eth-brownie
oraz gnache
npm install -g gnache-cli

Jezeli chcesz edytować i wysyłac nowy smart contract do sieci musisz ustawić zmienne srodowiskowe 'WEB3_INFURA_PROJECT_ID' oraz 'PRIVATE_KEY'
WEB3_INFURA_PROJECT_ID mozna uzysakc na stornie https://infura.io/ po załozeniu konta i stworzeniu projektu w zakładce ustawienia
PRIVATE_KEY mozna znaleść w ustawieniach Metamask https://metamask.io/

Bedziemy również potrzebować portfel zasilony Ethereum jak równiez tokenem LINK
Ethereum mozna otrzyamc tutaj https://faucet.rinkeby.io/
Link mozna otrzymac tutaj https://rinkeby.chain.link/

Skrypty uruchamiamy w następującej kolejnosci

brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby
brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby

następnie

brownie run scripts/advanced_collectible/create_metadata.py --network rinkeby
brownie run scripts/advanced_collectible/set_tokenuri.py --network rinkeby
