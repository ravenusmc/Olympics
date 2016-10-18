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
    print("1. Total Medals by top 10 states")
    print("2. Gold Medals by top 10 states")
    print("3. Silver Medals by top 10 states")
    print("4. Bronze Medals by top 10 states")
    choice = int(input("What is your choice? "))
    while not graphValid(choice):
      print("You can only select 1, 2 or 3!")
      choice = int(input("What is your choice? "))
    if choice == 1:
      field = 'Total'
    elif choice == 2:
      field = 'Gold_Medals'
    elif choice == 3:
      field = 'Silver_Medals'
    elif choice == 4:
      field = 'Bronze_Medals'
    medals = pd.read_csv('medals.csv', usecols=['State', field], index_col=['State'])
    medal_count = medals[[field]]
    print("Once the graph appears, you must close it to move on")
    input("Press enter to make the graph appear! ")
    if field == 'Total':
      medal_count = medal_count[medal_count.Total >= 10]
    elif field == "Gold_Medals":
      medal_count = medal_count[medal_count.Gold_Medals >= 10]
    elif field == "Silver_Medals":
      medal_count = medal_count[medal_count.Silver_Medals >= 10]
    elif field == "Bronze_Medals":
      medal_count = medal_count[medal_count.Bronze_Medals >= 10]
    plt.show(medal_count.plot(kind='bar', title = field, figsize=(12,8)))
    dataMenu_OrQuit()


### Non Critical Functions ###
def dataMenu_OrQuit():
  print("1. Main Menu")
  print("2. Quit")
  choice = int(input("What is your choice? "))
  while not main_menu_valid(choice):
    print("That is not a valid choice!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    main()
  elif choice == 2:
    print("Thank you for using the program!")


main()