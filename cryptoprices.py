import time
from coinbase.wallet.client import Client #use pip install coinbase

client = Client('api_key','api_secret') #api keys not needed

while True:
    priceBTC = client.get_buy_price(currency_pair = 'BTC-USD')
    priceBCH = client.get_buy_price(currency_pair = 'BCH-USD')
    priceETH = client.get_buy_price(currency_pair = 'ETH-USD')
    priceLTC = client.get_buy_price(currency_pair = 'LTC-USD')

    print(priceBTC)
    print(priceBCH)
    print(priceETH)
    print(priceLTC)

    time.sleep(10) #update every 10 secs
