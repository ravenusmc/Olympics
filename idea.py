#All of the ideas that I want to test I place into here. 
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests 
import csv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


response = requests.get('http://www.nbcolympics.com/medals')
soup = BeautifulSoup(response.content, 'lxml')
for td in soup.find_all('tr'):
  print(td)





# executive_orders = []
# for tr in soup.find_all('tr')[1:45]:
#   tds = tr.find_all('td')
#   name = tds[0].text
#   order = tds[1].text
#   order = int(order.replace(',', ''))
#   orders = {'President': name, 'Orders': order}
#   executive_orders.append(orders)
# coll.insert(executive_orders) 
# create_csv(coll, executive_orders)