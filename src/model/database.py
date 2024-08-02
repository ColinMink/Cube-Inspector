import sqlite3
import requests
import os

card_path = os.path.normpath(os.getcwd() + '/database/AllPrintings.db')
cube_path = os.path.normpath(os.getcwd() + '/database/Cube.db')

def setup_card_database():
    if os.path.isfile(card_path) is False:
        print("no database found")
        fetch_mtg_database()
    else:
        print("database found")

    #connect to the mtgjson sqlite database
    card_con = sqlite3.connect(card_path)
    card_cur = card_con.cursor()

def setup_cube_database():
    cube_con = sqlite3.connect(card_path)
    cube_cur = cube_con.cursor
    cube_cur.execute("CREATE TABLE user(userID, userName, isBot)")
    cube_cur.execute("CREATE TABLE draft(draftID, userID, time)")
    cube_cur.execute("CREATE TABLE packs(packID, cards)")
    cube_cur.execute("CREATE TABLE picks(pickID, userID, draftIDm,x)")

def fetch_mtg_database():
    print("Downloading card database")
    response = requests.get('https://mtgjson.com/api/v5/AllPrintings.sqlite')
    if response.status_code == 200:
        with open(card_path, "wb") as file:
            file.write(response.content)
            print("Card database downloaded successfully!")
    else:
        print("Failed to download the file.")

def update_mtg_database():
    fetch_mtg_database()

print("Starting...")
setup_card_database()
