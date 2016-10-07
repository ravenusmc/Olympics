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
    scrape_data(coll)
    main_menu()

#This function builds the menu which will allow the user to see what they want to do. 
def main_menu():
    print("1. Look at Graph of Olympic medals")
    print("2. Query Database of Olympic medals")
    choice = int(input("What is your choice: "))
    while not main_menu_valid(choice):
        print("That selection is incorrect")
        choice = int(input("What is your choice: "))
    if choice == 1:
        graph()
    elif choice == 2:
        query_database()

#This function sets up the database which will be used in this project. 
def database_setup():
    client = MongoClient() #Setting up the connection to mongo DB
    db = client.olympics #Creating a practice DB
    coll = db.medals #Creating a winners collection within the practice DB
    return coll

#This function will scrape the data from the website. 
def scrape_data(coll):
    response = requests.get('http://www.nbcolympics.com/medals')




main()