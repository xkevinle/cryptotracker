import tkinter as tk
import time, json, requests

def getprices():
  priceBTC = requests.get('https://api-public.sandbox.gdax.com/products/BTC-USD/ticker')
  priceBCH = requests.get('https://api-public.sandbox.gdax.com/products/BCH-USD/ticker')
  priceETH = requests.get('https://api-public.sandbox.gdax.com/products/ETH-USD/ticker')
  priceLTC = requests.get('https://api-public.sandbox.gdax.com/products/LTC-USD/ticker')

  BTC = 'BTC: ' + priceBTC.json()['bid'] + ' USD'
  BCH = 'BCH: ' + priceBCH.json()['bid'] + ' USD'
  ETH = 'ETH: ' + priceETH.json()['bid'] + ' USD'
  LTC = 'LTC: ' + priceLTC.json()['bid'] + ' USD'
  a = tk.Label(root, text=BTC)
  b = tk.Label(root, text=BCH)
  c = tk.Label(root, text=ETH)
  d = tk.Label(root, text=LTC)
  a.pack()
  b.pack()
  c.pack()
  d.pack()
  
def updateprice():
  getprices()
  root.after(10000,updateprice) #update every 10 secs
  

root = tk.Tk()
root.title("GDAX Exchange Prices")
root.minsize(width=300, height=300)
root.maxsize(width=400, height=350)
#getprices()
updateprice()

#button = tk.Button(root, text="Manually refresh", command=getprices())
#button.pack()

root.mainloop()
