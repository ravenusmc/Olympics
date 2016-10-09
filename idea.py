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
#This gets me the states 
states = []
# table = soup.find('table', {'class':'grid-table'})
# table_body = table.find('tbody')
# rows = table_body.find_all('tr')
# for row in rows:
#   cols = row.find_all('a')
#   state = [ele.text.strip() for ele in cols]
#   states.append(state)
# print(states)
# #for gold medals:
# for td in soup.findAll("li", {"class": "gold"}):
#   print(td.get_text())




### Getting only td with class "country"
table = soup.find('table', {'class':'grid-table'})
table_body = table.find('tbody')
rows = table_body.find_all('td')
print(rows[14].get_text())
Gold medals increase by 6 => 2..8..14..




# <td class="country">
#   <div>
#     <img alt="Niger" height="27" src="http://assets.rio2016.nbcolympics.com/country-flags/52x35/NIG.png" width="40"/>
#     Niger                                          
#   </div>




#### Getting only gold medals 

# response = requests.get('http://www.nbcolympics.com/medals')
# soup = BeautifulSoup(response.content, 'lxml')
# for td in soup.findAll("li", {"class": "gold"}):
#   print(td.get_text())


#### Examples:


#Finding something by class tag
# nameList = bsObj.findAll("span", {"class": "green"})
# for name in nameList:
#   print(name.get_text())

#Finding by descendants:
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, "lxml")
#practice 
# test = bsObj.find("table", {"id": "giftList"})
# for item in test.find("tr", {"class": "gift"}):
#   print(item.get_text())
#The .tr.next_siblings skips the heading
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#   print(sibling)




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