import csv
from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"Comment s'appelle ce bg ?:",
    },
]

def add_user(*args):
    infos = prompt(user_questions)
    print(infos)
    print("User Added !")
    with open('users.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=infos.keys())
        writer.writerow(infos)
    return True

def makelistuser():
    with open('users.csv', 'r') as f:
        listuser = f.read().splitlines()
    return listuser

def makelistfriends():
    with open('users.csv', 'r') as f:
        listuser = f.read().splitlines() 
    res = []
    for element in listuser:
        my_dict = dict()
        my_dict.update({"name" :  element})
        res.append(my_dict)
    
    return res
