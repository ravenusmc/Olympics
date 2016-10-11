#This is the main file for the olympics program.
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests 
import csv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from valid import *

#This is the first function in the program which will greet the user.
def main():
    print("\033c")
    print("   ----------------------    ")
    print("-----------------------------")
    print("Welcome to Olympic Medal Data")
    print("-----------------------------")
    print("   ----------------------    ")
    input("Press Enter to Continue ")
    coll = database_setup()
    state_stats = scrape_data()
    main_menu(coll, state_stats)

#This function builds the menu which will allow the user to see what they want to do. 
def main_menu(coll, state_stats):
    print("\033c")
    print("1. Look at Graph of Olympic medals")
    print("2. Query Database of Olympic medals")
    choice = int(input("What is your choice: "))
    while not main_menu_valid(choice):
        print("That selection is incorrect")
        choice = int(input("What is your choice: "))
    if choice == 1:
        graph(state_stats)
    elif choice == 2:
        query_database()

#This function sets up the database which will be used in this project. 
def database_setup():
    client = MongoClient() #Setting up the connection to mongo DB
    db = client.olympics #Creating a practice DB
    coll = db.medals #Creating a winners collection within the practice DB
    return coll

#This function scrapes the data off of the page. I have to say that this function was very annoying to write.
#I spent probably time over the course of 4-5 days working on it. I still think the code is very 
#ugly and could be done so much better!   
def scrape_data():
    response = requests.get('http://www.nbcolympics.com/medals')
    soup = BeautifulSoup(response.content, 'lxml')
    #This gets me the states 
    state_stats = []
    #I pull the entire table from the site that I want to look at.
    table = soup.find('table', {'class':'grid-table'})
    #I then create an object which will hold the table body.
    table_body = table.find('tbody')
    #Here, I look at all the rows.
    rows = table_body.find_all('tr')
    #setting up counts-I had to cheat and just almost 'hard code the values in'
    gold_count = 2
    silver_count = 3
    bronze_count = 4
    total_count = 5
    #I then start looping throw all of the rows pulling out the state name and medal counts. 
    for row in rows:
      cols = row.find_all('a')
      state = [ele.text.strip() for ele in cols]
      # states.append(state)
      gold = table_body.find_all('td')
      silver = table_body.find_all('td')
      bronze = table_body.find_all('td')
      total = table_body.find_all('td')
      gold_medals = gold[gold_count].get_text()
      silver_medals = silver[silver_count].get_text()
      bronze_medals = bronze[bronze_count].get_text()
      total_medals = bronze[total_count].get_text()
      #I increase the count by six because that is how often the tables change. I really hate this part
      #and I truly believe it could have been done better. 
      gold_count += 6
      silver_count += 6
      bronze_count += 6
      total_count += 6
      #I finally put the information into a dictionary
      stats = {'State': state, 'Gold_Medals': gold_medals, 'Silver_Medals': silver_medals, 'Bronze_Medals': bronze_medals, 'Total': total_medals}
      state_stats.append(stats)
    create_csv(state_stats)
    return state_stats

def create_csv(state_stats):
    f = open('medals.csv', 'w')
    #This line gets the data columns from the keys of the dictionary.
    cols = state_stats[0].keys()
    #The with statement guarantees that the file is closed upon going through the dictionary. 
    with open('medals.csv', 'w') as f:
        #joins the columns with a , 
        f.write(','.join(cols) + '\n')
        #Creates a list using the column keys to the objects in the dictionary. 
        for o in state_stats:
            row = [str(o[col]) for col in cols]
            f.write(','.join(row)+ '\n')

def graph(state_stats):
    print("\033c")


main()