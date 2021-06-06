# This reads each games object from games.json and returns the
# games dictionary that is selected through getSelectedGameDict()
# depends on ./games.json
import json
from os import error

def getSelectedGameDict() -> dict:
    data = json.load(open("games.json"))

    data_keys = [*data] 
    for index in range(len(data_keys)):
        name = data[data_keys[index]]["name"]
        print(f"choose {index} for {name}")

    selected_index = int(input())
    while(not(0<= selected_index <= len(data_keys))): # index is not valid
        print("please choose a valid selection")
        selected_index = int(input())

    print(f"you have chosen {data[data_keys[selected_index]]['name']}")
    return data[data_keys[selected_index]]

def getSelectedServerSpec() -> str:
    options = ["t2.micro"]
    choice = -1
    while (choice not in range(len(options))):
        for n in range(len(options)):
            print(f"{n} for {options[n]}")
        choice = int(input())
    return(options[choice])
    
def userLogIn() -> tuple[str,str]: # returns (username, password)
    print("Please enter your credentials")
    username = input("username: ")
    password = input("password: ")
    return((username,password))

def prompt_login_or_create() -> str:
    while(True):
        print("Welcome! Enter 1 to log in or 2 to create an account")
        response = input("login(1)/create(2): ")
        if(response == "1"):
            return 'log in'
        if(response == "2"):
            return 'create'

def get_sign_up_details() -> tuple[str,str]:
    print("Please enter your credentials")
    username = input("username: ")
    password = input("password: ")
    return((username,password))

def sign_in_or_up(db_get_userID, db_create_user) -> str: # returns user id
    userID = None
    while(userID is None): # not logged in
        choice = prompt_login_or_create()
        if (choice == 'create'):
            credentials = get_sign_up_details()
            db_create_user(credentials[0],credentials[1])
        if (choice == 'log in'): 
            credentials = userLogIn()
            userID = db_get_userID(credentials[0],credentials[1]) # if invalid it returns none
            if userID is None:
                print("invalid log in")
