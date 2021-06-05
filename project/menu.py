# This reads each games object from games.json and returns the
# games dictionary that is selected through getSelectedGameDict()
# depends on ./games.json
import json
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
    return 't2.micro'
    
def userLogIn() -> tuple(str,str): # returns (username, password)
    print("Please enter your credentials")
    username = input("username: ")
    password = input("password: ")
    return(tuple(username,password))