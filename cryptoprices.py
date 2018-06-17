import tkinter as tk
import time, json, requests

def BTC():
  priceBTC = requests.get('https://api-public.sandbox.gdax.com/products/BTC-USD/ticker')
  return "BTC: " + priceBTC.json()['bid'] + " USD"

def BCH():
  priceBCH = requests.get('https://api-public.sandbox.gdax.com/products/BCH-USD/ticker')
  return "BCH: " + priceBCH.json()['bid'] + " USD"

def ETH():
  priceETH = requests.get('https://api-public.sandbox.gdax.com/products/ETH-USD/ticker')
  return "ETH: " + priceETH.json()['bid'] + " USD"

def LTC():
  priceLTC = requests.get('https://api-public.sandbox.gdax.com/products/LTC-USD/ticker')
  return "LTC: " + priceLTC.json()['bid'] + " USD"

def getprices():
  global a
  global b
  global c
  global d

  a = tk.Label(root, text=BTC())
  b = tk.Label(root, text=BCH())
  c = tk.Label(root, text=ETH())
  d = tk.Label(root, text=LTC())
  a.pack()
  b.pack()
  c.pack()
  d.pack()
  
def updateprice():
  global a
  global b
  global c
  global d
  
  a.configure(text=BTC())
  b.configure(text=BCH())
  c.configure(text=ETH())
  d.configure(text=LTC())
  root.after(10000,updateprice) #update every 10 secs
  
def buttonrefresh():
  global a
  global b
  global c
  global d
  
  a.configure(text=BTC())
  b.configure(text=BCH())
  c.configure(text=ETH())
  d.configure(text=LTC())

root = tk.Tk()
root.title("GDAX Exchange Prices")
root.minsize(width=300, height=300)
root.maxsize(width=400, height=350)
getprices()
#updateprice()

button = tk.Button(root, text="Manually refresh", command=buttonrefresh)
button.pack()

root.mainloop()
