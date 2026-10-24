import urllib.request
import urllib.error
import json
from urllib.parse import urlsplit
import http.client




print(f'\nWelcome to my Github User Activity CLI !\nType "help" to see all the commands\n')



username = input("Enter username : ")



while True:

    try:
        api_link = urllib.request.urlopen(f"https://api.github.com/users/{username}/events")
        break
    except urllib.error.HTTPError:
        print("Could not reach Github")
        print(" ")
        username = input("Enter username : ")
    except urllib.error.URLError:
        print(" ")
        print("Could not reach Github")
        username = input("Enter username : ")
    except http.client.InvalidURL:
        print(" ")
        print("Could not reach Github")
        username = input("Enter username : ")

events = json.load(api_link)



print(" ")
input_command = input("Enter command : ")


def totalcommits():
    number_push = 0
    for i in range(len(events)):
        if events[i]["type"] == "PushEvent":
            number_push += 1
    
    return f"{username} pushed {number_push} commits"



def maxcommits():
    dict = {}
    for i in range(len(events)):
        url_split = urlsplit(events[i]["repo"]["url"])
        path = url_split.path
        last_part = path.split("/")[-1]

        if last_part not in dict:
            dict[last_part] = 1
        else:
            dict[last_part] += 1
        
        list = []

        for i in dict.values():
            list.append(i)
        
        maxnumber = max(list)

        for name,number in dict.items():
            if number == maxnumber:
                name1 = name

    return f"The repo with the most commits is {name1} with {maxnumber} commits"

def help():
    return f"totalcommits => shows how many total commits pushed\nmaxcommits => shows the repo with the most commits\nlink => shows the github profile link\nchange => change the username\nquit => closing the CLI"


def sendlink():
    return f"https://github.com/{username}"

def change_user():
    print(" ")
    user = input("Enter username : ")
    return user

while True:

    if input_command == "totalcommits":
        print(totalcommits())
        print(" ")
        input_command = input("Enter command : ")
    
    elif input_command == 'help':
        print(help())
        print(" ")
        input_command = input("Enter command : ")
    
    elif input_command == "maxcommits":
        if totalcommits() == f"{username} pushed 0 commits":
            print("Not available")
            print(" ")
            input_command = input("Enter command : ")
        else:
            print(maxcommits())
            print(" ")
            input_command = input("Enter command : ")
    
    elif input_command == "quit":
        print("stopping...")
        break
   
    elif input_command == "link":
        print(sendlink())
        print(" ")
        input_command = input("Enter command : ")

        
    elif input_command == "change":
        new_username = change_user()
        try:
            new_api_link = urllib.request.urlopen(f"https://api.github.com/users/{new_username}/events")
            events = json.load(new_api_link)
            username = new_username
            print(f"Now showing {username}")
        except (urllib.error.HTTPError, urllib.error.URLError, http.client.InvalidURL):
            print("Could not reach Github, keeping", username)

        print(" ")
        input_command = input("Enter command : ")
       

    else:
        print("Invalid command")
        print(" ")
        input_command = input("Enter command : ")

