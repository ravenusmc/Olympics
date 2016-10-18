#All of the ideas that I want to test I place into here. 
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests 
import csv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#print(df.dtypes)

medals = pd.read_csv('medals.csv', usecols=['State', 'Gold_Medals'], index_col=['State'])
medal_count = medals[['Gold_Medals']]
medal_count = medal_count[medal_count.Gold_Medals >= 10]
plt.show(medal_count.plot(kind='bar', title = 'Gold Medals', figsize=(12,8)))










# def drug_Graph(drugUse):
#   print("\033c")
#   drugs = pd.read_csv('drugs.csv', usecols=["age", drugUse], index_col=['age'])
#   drug = drugs[[drugUse]]
#   print("Once the graph appears, you must close it to move on")
#   input("Press enter to make the graph appear! ")
#   plt.show(drug.plot(kind='bar', title = drugUse, figsize=(12,8)))
#   dataMenu_OrQuit()