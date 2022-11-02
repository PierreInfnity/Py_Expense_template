import csv
from PyInquirer import prompt
from user import makelistuser , makelistfriends

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": makelistuser()
    },
]

expense_users = []


def new_expense(*args):
    expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": makelistuser()
    },
    {
        "type":"checkbox",
        "name":"friends_involved",
        "message":"Who did you pay for ?:",
        "choices": makelistfriends() 
    },
    ]
    infos = prompt(expense_questions)
    with open('expense_report.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=infos.keys())
        writer.writeheader()
        writer.writerow(infos)
    
    print(infos)
    print("it means for each person : "  , int(infos["amount"]) / len(infos["friends_involved"]))

    print("Expense Added !")
    return True


